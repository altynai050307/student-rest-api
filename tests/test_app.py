from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == "Student REST API is running"


def test_get_students():
    client = app.test_client()

    response = client.get("/students")

    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) >= 3


def test_get_existing_student():
    client = app.test_client()

    response = client.get("/students/1")

    assert response.status_code == 200
    assert response.json["id"] == 1


def test_get_non_existing_student():
    client = app.test_client()

    response = client.get("/students/999")

    assert response.status_code == 404