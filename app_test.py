import os
import pytest
import json
from app import load_data, save_data, create_user, update_user, delete_user

@pytest.fixture
def setup_data():
    test_data = [{"name": "Test User", "email": "test@example.com"}]
    save_data(test_data)
    yield
    if os.path.exists("registrations.json"):
        os.remove("registrations.json")

def test_create_user(setup_data):
    create_user("New User", "newuser@example.com")
    data = load_data()
    assert len(data) == 2
    assert data[-1]['name'] == "New User"

def test_update_user(setup_data):
    update_user("test@example.com", "Updated User", "updated@example.com")
    data = load_data()
    assert len(data) == 1
    assert data[0]['name'] == "Updated User"
    assert data[0]['email'] == "updated@example.com"

def test_delete_user(setup_data):
    delete_user("test@example.com")
    data = load_data()
    assert len(data) == 0

def test_read_users(setup_data):
    data = load_data()
    assert len(data) == 1
    assert data[0]['name'] == "Test User"
