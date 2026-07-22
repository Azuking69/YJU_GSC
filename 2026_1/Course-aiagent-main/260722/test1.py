import json
from pydantic import BaseModel, ValidationError
from typing import Literal

# pydantic -> schema
class Student(BaseModel):
    id:int
    grade:Literal["1","2","3"]

try:
    rcvd_data = '{"id": 1, "name": "gsc", "grade": "4"}'
    obj = Student.model_validate_json(rcvd_data)
    print(obj)
except ValidationError:
    print("예외처리")

