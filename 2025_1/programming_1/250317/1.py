
#함수를 만든다...?
print("hello") #함수를 호출한다.

#1. 함수 정의/선어
say_something : 
#   입력값 x -> 알고리즘 [안녕하세요] -> 출력값 하면에 문자열 출력

#def 명령어는 새로운 함수 정의를 의미한다.
def say_something() : 
   #메모리에 등록 이름(say_something), 안에 알고리즘(print("안녕하세요"))
   print("안녕하세요")

#2. 함수 호출
#say_something()

def add(x, y):
    result = x + y
    return result #return : 호출한 위치에 돌아간다

result1 = add(2, 3)
result2 = add(5, 6)
print(f"result1: {result1}, result2:{result2}")