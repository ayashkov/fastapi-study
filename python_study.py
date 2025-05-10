from pathlib import Path
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from spa import SinglePageApplication

app = FastAPI()
api = FastAPI()
app.mount("/api/v1", api)
app.mount("/", SinglePageApplication(directory=Path("www")), name="Angular")


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@api.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@api.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
