import os, json
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, text
import redis

app = FastAPI()
engine = create_engine(os.environ["DATABASE_URL"], pool_pre_ping=True)
cache = redis.Redis(host=os.environ["REDIS_HOST"], port=6379, decode_responses=True)

with engine.begin() as conn:
    conn.execute(text(
        "CREATE TABLE IF NOT EXISTS items (id serial PRIMARY KEY, name text)"))

class Item(BaseModel):
    name: str

@app.post("/items")
def add_item(item: Item):
    with engine.begin() as conn:
        conn.execute(text("INSERT INTO items (name) VALUES (:n)"), {"n": item.name})
    cache.delete("items")
    return {"ok": True, "name": item.name}

@app.get("/items")
def list_items():
    cached = cache.get("items")
    if cached is not None:
        return {"source": "cache", "items": json.loads(cached)}
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT id, name FROM items ORDER BY id")).mappings().all()
    items = [dict(r) for r in rows]
    cache.setex("items", 10, json.dumps(items))
    return {"source": "db", "items": items}
