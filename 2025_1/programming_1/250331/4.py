#변수의 scope 괌점
# -Gloval variable(전역변수)
#  -> 함수 밖에서 선어된 변수
#  ->B : 변수 선어
#  ->D : 프로그댐 종료 시
# -Local variable(지녁변수)
#  -> 함수 내 선어된 변수
 

def getname(arg_name):
    return arg_name + "님"

def getGreeting(arg_name):
    greeting = arg_name + "안녕하세요"
    return greeting

def prtShow(arg_name):
    name = getname(arg_name)
    msg = getGreeting(name)
    print(f"name: {name} -> msg: {msg}")

prtShow("홍길동")

"""
def show_image(arg_file_name):
    pass

print(msg)"
"""