class Bar:
    #클래스멤버변수 = "클래스변수"
    id = 123 #클래스 멤버 변수

    def __init__(self, arg_name, arg_age):
        self.name = arg_name # 인스턴스멤버변수
        self.age = arg_age 

obj_1 = Bar("김철수", 23)
obj_2 = Bar("김영희", 20)
print(obj_1.name, obj_1.age, obj_1.id)
print(obj_2.name, obj_2.age, obj_2.id)