import json
from pydantic import BaseModel, ValidationError
from typing import Literal

# pydantic -> schema
class Student(BaseModel):
    id:int
    grade:Literal["1","2","3"]

try:
    rcvd_data = '{"id": 1, "name": "gsc", "grade": "3"}'
    obj = Student.model_validate_json(rcvd_data)
    print(obj)
    print()
    print(obj.model_dump_json())
except ValidationError:
    print("예외처리")

