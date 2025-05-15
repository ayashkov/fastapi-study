from uvicorn import run

from fastapi_study.app import app


def main() -> None:
    run(app, host="0.0.0.0")
