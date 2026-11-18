# Decorator

def log(func):
    print("로그 함수 실행")
    return func

@log # -> 1) log(test) -> 2) test = log(test)
def test():
    print("test 함수 실행")


test()