from collections.abc import Generator

def test():
    print("test 호출")
    yield 3
    yield 4
    print("test 종료")
    yield 5

generator_obj = test()

itr = iter(generator_obj)

print(next(itr), "\n\n") # 3
print(next(itr)) # 4
print(next(itr)) # StopIteration 발생