# of parameter od  the test function
# conduct packing for the arguments
def test(*args):
    for val in args:
        print(val, end="\t")

test(1)
test(1, 2)
test(1, 2, 3)
test(1, 2, 3, 4)