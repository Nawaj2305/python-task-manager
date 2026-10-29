import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as test_client:
        yield test_client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Python Task Manager" in response.data


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_get_tasks(client):
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_create_task(client):
    response = client.post(
        "/api/tasks",
        json={"title": "Practice Docker"}
    )

    assert response.status_code == 201
    assert response.json["title"] == "Practice Docker"
    assert response.json["completed"] is False


def test_create_task_without_title(client):
    response = client.post("/api/tasks", json={"title": " "})
    assert response.status_code == 400


def test_update_task(client):
    response = client.patch(
        "/api/tasks/1",
        json={"completed": True}
    )

    assert response.status_code == 200
    assert response.json["completed"] is True


def test_update_missing_task(client):
    response = client.patch(
        "/api/tasks/999",
        json={"completed": True}
    )

    assert response.status_code == 404