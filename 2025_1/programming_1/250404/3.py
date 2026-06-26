bar = 3

def test():
    global bar
    #전역 변수 bar의 값을 1 증가 하고 싶어
    bar = 4

test()
print(bar) #4

