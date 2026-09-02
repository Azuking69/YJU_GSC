class Bar:
    """
        1) 생성자
        2) 멤버 변수
        3) 멤버 메소드
        4) 소멸자
    """

    # self: 매개 변수 -> 
    # 참조 변수: 현재 생성된 인스턴스의 주소
    def __init__(self):
        print(self)
        print(isinstance(self, Bar))

Bar()