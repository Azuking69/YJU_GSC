import pydantic from BaseModel1

class MyClass(BaseModel1):
    name: str
    age: int

print(MyClass.model_json_schema())