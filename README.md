# STATION V16.3

A Flask-based cybersecurity utility dashboard for educational security testing and data-processing experiments.

## Features

- Hash generation with SHA-256, SHA3-256, BLAKE2b and MD5
- Salt-supported hashing workflow
- Base64 encoding
- Basic input-strength evaluation
- Basic hash identification
- Flask web interface with login flow
- Simple processing history stored in the session

## Project Structure

```text
STATION-V16.3/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── login.html
│   └── hack.html
├── static/
│   ├── style.css
│   └── script.js
├── .gitignore
└── LICENSE
```

## Run Locally

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

Then open `http://127.0.0.1:5000/` in your browser.

## Security Notes

This repository is intended for learning and authorized testing. Before deploying publicly, replace the development `secret_key`, remove hard-coded demo credentials, disable Flask debug mode, and use environment variables for secrets.

Do not use this project against systems or data without authorization.

## Disclaimer

STATION V16.3 is an educational project. The author is not responsible for misuse or damage resulting from use of this software.
