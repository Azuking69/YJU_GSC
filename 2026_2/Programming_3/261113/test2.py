from collections.abc import Generator

def test():
    print("test 호출")
    yield 3
    print("test 종료")

itr = iter(test())