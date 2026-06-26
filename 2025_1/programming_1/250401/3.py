#변수
#1)지역변수
#2)전역변수

#접근범위, 생명주기

def c():
    print("c 함수 호출")
    print("c 함수 종료")

def b():
    print("b 함수 호출")
    c() 
    print("b 함수 종료")

def a():
    print("a 함수 호출")
    b()
    print("a 함수 종료")

a()