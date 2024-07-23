import requests
import pytest

BASE_URL = "http://localhost:8000/api/user"


def test_get_user_1():
    response = requests.get(f"{BASE_URL}/1")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == 1
    assert data["data"]["email"] == "george.bluth@reqres.in"
    assert data["data"]["first_name"] == "George"
    assert data["data"]["last_name"] == "Bluth"


def test_get_user_2():
    response = requests.get(f"{BASE_URL}/2")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == 2
    assert data["data"]["email"] == "janet.weaver@reqres.in"
    assert data["data"]["first_name"] == "Janet"
    assert data["data"]["last_name"] == "Weaver"


def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/999")
    assert response.status_code == 404
    data = response.json()
    assert data["error"] == "User not found"


def test_invalid_user_id():
    response = requests.get(f"{BASE_URL}/abc")
    assert response.status_code == 422
