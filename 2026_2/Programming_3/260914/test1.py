class Foo:
    def __init__(self): # 생성자 Constructure
        print("Foo 생성")

    # Magic Method, Magic member variable
    def __del__(self): # 소멸자 Destructor
        print("Foo 소멸")


Foo() # 생성자 호출, 소멸자 호출