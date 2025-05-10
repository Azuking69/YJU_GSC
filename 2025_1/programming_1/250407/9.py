a, b, c, = 5, 6, 10
result = a < b < c #True, a는 b보다 작고 b는 c보다 작다.
print(result)

x = 20
if 10 < x < 30:
    print("x는 10과 30 사이에 있습니다.") #출력됨


y = 15
if 5 < y <= 20:
    print("y는 5 초과 20 이하입니다.") #출력됨

print(2 < 3 < 5 < 6 < 7) #True