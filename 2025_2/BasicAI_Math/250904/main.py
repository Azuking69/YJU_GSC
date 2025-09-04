import math

# 係数
a, b, c = 2, -3, -2

# 判別式
D = b ** 2 - 4 * a * c

# 解の計算
x1 = (-b + math.sqrt(D)) / (2 * a)
x2 = (-b - math.sqrt(D)) / (2 * a)

# 和と積
sum_roots = x1 + x2
product_roots = x1 * x2

print("解: ", x1, x2)
print("a + b =", sum_roots)
print("a X b =", product_roots)
