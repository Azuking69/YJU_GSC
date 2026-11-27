def my_decorator(func):
    return func

class Bar:
    class foo:
        ...
    ...


# closer function
def test():
    msg = "GSC"
    # nested function
    def inner_function():
        print(f"{msg} inner function")

    print("test!!!")
    return inner_function

test()()  # call the returned function
test()()  # call the returned function again
