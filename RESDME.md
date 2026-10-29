# Python Task Manager

An open-source task management web application built using
Python, Flask, and Docker.

## Features

- Flask web interface
- REST API for tasks
- Application health endpoint
- Automated tests with pytest
- Code linting with Ruff
- Docker container support
- GitHub Actions CI/CD
- Docker image publishing to GHCR

## Run locally

```bash
python -m venv .venv
pip install -r requirements-dev.txt
python run.py