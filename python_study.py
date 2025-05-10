from pathlib import Path

from fastapi import FastAPI

from api import api
from spa import SinglePageApplication

app = FastAPI()
app.include_router(api, prefix="/api/v1")
app.mount("/", SinglePageApplication(directory=Path("www")), name="Angular")
