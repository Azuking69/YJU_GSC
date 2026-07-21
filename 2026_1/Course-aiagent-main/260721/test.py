from pydantic import BaseModel
from typing import Literal

class car(BaseModel):
    model: str
    year: int
    c_type: Literal[ "suv", "sedan", "pickup"]

bar = car(model="x7", year=2026, c_type="suv")

print(bar.model_dump_json())