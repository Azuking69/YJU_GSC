def my_range(start, stop):
    cnt = start

    while cnt < stop:
        yield cnt
        cnt += 1


try:
    gen_obj = my_range(2, 5)
    itr = iter(gen_obj)

    while True:
        print(next(itr))

except StopIteration as e:
    print(e)

# for value in my_range(2, 5):
#     print(value)