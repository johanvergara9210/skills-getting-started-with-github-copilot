import copy
import pytest
from fastapi.testclient import TestClient

# Import app and activities reference from src.app
from src.app import app, activities as activities_ref

@pytest.fixture
def client():
    """Test client for the FastAPI app"""
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activities dict before/after each test"""
    backup = copy.deepcopy(activities_ref)
    try:
        yield
    finally:
        activities_ref.clear()
        activities_ref.update(copy.deepcopy(backup))
