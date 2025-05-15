from fastapi import FastAPI

from fastapi_study.api import api
from fastapi_study.spa import SinglePageApplication

app = FastAPI()
app.include_router(api, prefix="/api/v1")
app.mount("/", SinglePageApplication(packages=["fastapi_study.ui"]),
    name="Angular")
