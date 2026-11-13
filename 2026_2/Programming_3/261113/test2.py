from collections.abc import Generator

def test():
    print("test 호출")
    yield 3
    print("test 종료")

generator_obj = test()

itr = iter(test())

print(next(itr)) # 3
print(next(itr)) # StopIteration 발생