result_1 = [x for x in range(5)] # 리스트 컴프리헨션
print(result_1) # [0, 1, 2, 3, 4]

result_2 = (x for x in range(5)) # 제너레이터 표현식
# def anoymous():
#     for x in range(5):
#         yield x

# print(result_2) # <generator object <genexpr> at 0x000001F3D8A1B5C0>
print(next(result_2)) # 0
print(next(result_2)) # 1
print(next(result_2)) # 2