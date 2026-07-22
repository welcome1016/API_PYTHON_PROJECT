# Travel API Project

## Overview

This project is a simple RESTful API for managing travel destinations. It is built with Python and Flask, using SQLAlchemy for database access and SQLite as the local database.

## Tech Stack

- Python 3.14
- Flask 3.1.3
- Flask-SQLAlchemy 0.6
- SQLite (local database)
- HTML/JSON API responses

## Features

- CRUD operations for travel destinations
- JSON-based API endpoints
- Local SQLite persistence
- Automatic database creation on first run

## Dependencies

Dependencies are listed in `requirements.txt` and include:

- blinker==1.9.0
- click==8.4.2
- colorama==0.4.6
- Flask==3.1.3
- Flask-SQLAlchemy==0.6
- itsdangerous==2.2.0
- Jinja2==3.1.6
- MarkupSafe==3.0.3
- setuptools==83.0.0
- Werkzeug==3.1.8

## Installation

1. Create and activate the virtual environment:

```powershell
python -m venv api-env
.\
api-env\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

## Run the API

Start the application:

```powershell
python main.py
```

The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

- `GET /` - Welcome message
- `GET /destinations` - List all destinations
- `GET /destinations/<id>` - Retrieve a destination by ID
- `POST /destinations` - Create a new destination
- `PUT /destinations/<id>` - Update an existing destination
- `DELETE /destinations/<id>` - Delete a destination

## Notes

- The application creates `travel.db` automatically in the project root when launched.
- Use JSON body payloads for `POST` and `PUT` requests.

## Example JSON Payload

```json
{
  "destinations": "Paris",
  "country": "France",
  "rating": 4.8
}
```
