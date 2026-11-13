from collections.abc import Generator

def test():
    print("테스트 시작")
    yield 10
    print("테스트 10 종료")
    yield 20
    print("테스트 종료")

iter = test()

print(next(iter))
print(next(iter))
print(next(iter))