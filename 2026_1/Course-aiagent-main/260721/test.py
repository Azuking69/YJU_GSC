from pydantic import BaseModel, validationError
from typing import Literal

# value -> validation -> object
class car(BaseModel):
    model: str
    year: int
    c_type: Literal[ "suv", "sedan", "pickup"]

try:
    bar = car(model="x7", year=2026, c_type="truck")
except validationError:
    print("데이터 에러")


# json -> object

# print(bar.model_dump_json())