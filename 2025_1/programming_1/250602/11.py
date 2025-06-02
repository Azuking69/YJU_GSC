# 함수 정의
# -> 자기만의 함수를 만들고 싶을 때

# bar 함수 정의
def prt_elements(*args): # -> len(args)
    last_index = len(args) - 1
    msg = "[ "
    for val in args:
        msg += str(val) + ',' if idx != last_index else str(val)
    msg += " ]"
    print(msg)


# bar 함수 호출
prt_elements() # -> 0, []
prt_elements(1) # -> 1, [1]
prt_elements(1, 100) # -> 2, [1, 100]
prt_elements(1, 100, 2, 300) # -> 3, [1, 100, 2, 300]