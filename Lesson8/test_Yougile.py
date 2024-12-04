import pytest
from YougileApi import Yougile

api = Yougile()

# Позитивные тесты

def test_create_project():
    result = api.create_project("New Project")
    assert result.status_code == 201
    assert "id" in result.json()

def test_get_all_projects():
    response = api.get_all_projects()
    assert response.status_code == 200

def test_get_project_by_id():
    create_project = api.create_project("New Project")
    new_id = create_project.json()["id"]
    response = api.get_project_by_id(new_id)
    assert response.status_code == 200
    assert response.json()["title"] == "New Project"

def test_update_project_title():
    create_project = api.create_project("Very new Project")
    new_id = create_project.json()["id"]
    update_project = api.update_project_title("Very new Project updated", new_id)
    response = api.get_project_by_id(new_id)
    assert response.status_code == 200
    assert response.json()["title"] == "Very new Project updated"


# Негативные тесты

def test_create_project_no_title():
    result = api.create_project("")
    assert result.status_code == 400

def test_create_project_invalid_title():
    result = api.create_project("1253^%$jdhg")
    assert result.status_code == 400

def test_get_project_by_invalid_id():
    invalid_id = "jhg73652kfgj"
    response = api.get_project_by_id(invalid_id)
    assert response.status_code == 404
