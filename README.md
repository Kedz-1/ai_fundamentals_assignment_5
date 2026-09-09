# Mini Issue Tracker API

A small FastAPI application for creating, viewing, updating, and deleting
issues. Issues are stored in memory, so they are reset whenever the application
restarts.

## Installation

Python 3.11 or later is recommended.

```bash
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Running the API

From the repository root, start the development server with:

```bash
uvicorn src.main:app --reload
```

The API is available at `http://127.0.0.1:8000`, and interactive documentation
is available at `http://127.0.0.1:8000/docs`.

## Running the tests

```bash
PYTHONPATH=. pytest -v test/
```

## Issue endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `POST` | `/issues` | Create an issue |
| `GET` | `/issues` | List, search, or filter issues |
| `GET` | `/issues/{issue_id}` | Retrieve one issue |
| `PATCH` | `/issues/{issue_id}` | Update an issue |
| `DELETE` | `/issues/{issue_id}` | Delete an issue |

Create an issue with a JSON body containing a title, description, and optional
status:

```bash
curl -X POST http://127.0.0.1:8000/issues \
  -H "Content-Type: application/json" \
  -d '{"title":"Login error","description":"Users cannot sign in","status":"Open"}'
```

## Searching and filtering issues

`GET /issues` accepts two optional query parameters:

- `search` performs a case-insensitive substring search across issue titles and
  descriptions.
- `status` performs a case-insensitive exact match against issue status.

Use either filter independently:

```bash
curl "http://127.0.0.1:8000/issues?search=login"
curl "http://127.0.0.1:8000/issues?status=closed"
```

Or combine them; an issue must satisfy both filters to be returned:

```bash
curl "http://127.0.0.1:8000/issues?search=login&status=open"
```

Calling `GET /issues` without query parameters continues to return every issue.
If no issues match the supplied filters, the response is an empty JSON list:

```json
[]
```
