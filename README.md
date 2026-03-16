# Student API — Mini CRUD demo

**Benjamin Attuah-Odei** — Junior Software Engineer demo repo.

## What this is
A minimal REST API (Flask + SQLite) that implements CRUD for a `Student` resource. Includes a small frontend that interacts with the API and a simple `backup.sh` utility.

## Tech
- Python, Flask
- SQLite (lightweight SQL DB; SQL skills demonstrated)
- HTML/JS frontend (fetch)
- Bash automation script

## Quick start (local)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
# open frontend/index.html in your browser or visit http://127.0.0.1:5000 if you want only the API
```

## Endpoints
- `GET /students` — list
- `POST /students` — create (JSON: {name, email})
- `GET /students/<id>` — details
- `PUT /students/<id>` — update
- `DELETE /students/<id>` — delete

## Demo helpers
- `python3 create_sample_db.py` — creates `students.db` with sample data (table name `student`) for quick testing if you don't want to run the API.
- `scripts/backup.sh <folder>` — create a tar.gz backup of a folder.

## License & attribution
This repo is created as an example to demonstrate backend + SQL + frontend fundamentals. Adapt and extend freely; if you borrow code from other repos, include attribution in this README.

## Contact
Benjamin Attuah-Odei — benjaminattuahodei@gmail.com 
