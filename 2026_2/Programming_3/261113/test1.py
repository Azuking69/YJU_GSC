def test():
    print("test 호출")
    # yield 3
    print("test 종료")

test()

class Bar:
    def prd_spmething(self):
        print("prd_something 호출")
        # yield 3
        print("prd_something 종료")


obj = Bar()
obj.prd_spmething()