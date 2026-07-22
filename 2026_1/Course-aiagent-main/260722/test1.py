from pydantic import BaseModel
from typing import Literal

# pydantic -> schema
class Student(BaseModel):
    id:int
    grade:Literal["1","2","3"]

obj = Student(id=1, name="gsc", grade="2")

print(obj)