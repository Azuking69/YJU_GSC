def test(a, b, c, d):
    print(f"a: {a}")
    print(f"a: {b}")
    print(f"a: {c}")
    print(f"a: {d}")

# bar = [1, 2, 3, 4]
foo = {'d':10, 'b':2, 'c':4, 'a':1}
test(**foo)


# def get_sum_avg(a, b):
#     sum = a + b
#     avg = sum / 2
#     return sum, avg

# # unpacking
# sum, avg = get_sum_avg(1, 2)
# print(sum, avg)