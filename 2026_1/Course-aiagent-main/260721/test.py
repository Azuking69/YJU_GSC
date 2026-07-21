from pydantic import BaseModel, ValidationError
from typing import Literal

# value -> validation -> object
class Car(BaseModel):
    model: str
    year: int
    c_type: Literal["suv", "sedan", "pickup"]

try:
    # bar = Car(model="x7", year=2026, c_type="truck")
    bar = {"model": "x3", "year": 2024, "c_type": "sedan"}
    # json -> parse -> validator -> object
    obj = Car.model_validate_json(bar)
    print(obj.model_dump_json())

except ValidationError:
    print("데이터 에러")


# json -> object


# print(bar.model_dump_json())