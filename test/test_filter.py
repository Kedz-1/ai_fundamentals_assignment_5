import pytest
from fastapi.testclient import TestClient

from src.main import app, issues


@pytest.fixture(autouse=True)
def clear_issues():
    issues.clear()
    yield
    issues.clear()


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def populated_client(client):
    issue_data = [
        {
            "title": "Login page failure",
            "description": "Users cannot sign in",
            "status": "Open",
        },
        {
            "title": "Update dashboard",
            "description": "Fix the LOGIN activity widget",
            "status": "Closed",
        },
        {
            "title": "Improve reports",
            "description": "Add export controls",
            "status": "In Progress",
        },
    ]
    for issue in issue_data:
        client.post("/issues", json=issue)
    return client


def test_search_matches_titles_case_insensitively(populated_client):
    response = populated_client.get("/issues", params={"search": "LOGIN PAGE"})

    assert response.status_code == 200
    assert [issue["title"] for issue in response.json()] == ["Login page failure"]


def test_search_matches_descriptions_case_insensitively(populated_client):
    response = populated_client.get("/issues", params={"search": "login activity"})

    assert response.status_code == 200
    assert [issue["title"] for issue in response.json()] == ["Update dashboard"]


def test_status_filter_is_case_insensitive(populated_client):
    response = populated_client.get("/issues", params={"status": "in progress"})

    assert response.status_code == 200
    assert [issue["title"] for issue in response.json()] == ["Improve reports"]


def test_search_and_status_filters_can_be_combined(populated_client):
    response = populated_client.get(
        "/issues", params={"search": "login", "status": "CLOSED"}
    )

    assert response.status_code == 200
    assert [issue["title"] for issue in response.json()] == ["Update dashboard"]


def test_filters_return_empty_list_when_no_issue_matches(populated_client):
    response = populated_client.get("/issues", params={"search": "printer"})

    assert response.status_code == 200
    assert response.json() == []


def test_no_filters_still_returns_every_issue(populated_client):
    response = populated_client.get("/issues")

    assert response.status_code == 200
    assert len(response.json()) == 3


def test_empty_search_matches_every_issue(populated_client):
    response = populated_client.get("/issues", params={"search": ""})

    assert response.status_code == 200
    assert len(response.json()) == 3
