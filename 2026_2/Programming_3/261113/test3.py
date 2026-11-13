def my_range(start, stop):
    cnt = start

    while cnt < stop:
        yield cnt
        cnt += 1


obj = my_range(2, 5)
print(type(obj))

itr = iter(obj)
print(type(itr))