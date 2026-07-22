from pydantic import BaseModel, ValidationError
from typing import Literal

# pydantic -> schema
class Student(BaseModel):
    id:int
    grade:Literal["1","2","3"]

try:
    obj = Student(id=1, name="gsc", grade="4")
except ValidationError:
    print("예외처리")

print(obj)