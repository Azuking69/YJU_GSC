import math

# 계산식 정의
def solve_quadratic(a, b, c):
    # 판별식
    D = b ** 2 - 4 * a * c
    
    # 서로 다른 두 실근
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return (x1, x2)
    
    # 중근
    elif D == 0:
        x = -b / (2 * a)
        return x
    
    # 서로 다른 두 허근
    else:
        return ("허수해가 있다")
    

# 1. y = x**2 - 4x + 3
print("y = x**2 - 4x + 3: ", solve_quadratic(1, -4, 3))
# 2. y = - x**2 + 4x - 3
print("y = - x**2 + 4x - 3: ", solve_quadratic(-1, 4, -3))
# 3. y = x**2 + 8x + 12
print("y = x**2 + 8x + 12: ", solve_quadratic(1, 8, 12))
# y = x**2 - 2x + 1
print("y = x**2 - 2x + 1: ", solve_quadratic(1, -2, 1)) 