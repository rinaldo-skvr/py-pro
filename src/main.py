from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None

@app.get("/")
def read_root():
    return {"message": "Hello, 3Netra POC API!"}

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

# Start up command:
# uvicorn main:app --reload