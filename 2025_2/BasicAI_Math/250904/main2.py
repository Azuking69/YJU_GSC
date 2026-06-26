import numpy as np
import matplotlib.pyplot as plt
import math

# 2차방정식 해 구하는 함수
def solve_quadratic(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return [x1, x2]
    elif D == 0:
        x = -b / (2 * a)
        return [x]
    else:
        return []  # 허근은 그리지 않음

# 画像に出ていた6つのケース
cases = [
    (1, -4, 3),
    (-1, 4, -3),
    (1, 8, 12),
    (1, -2, 1),
    (2, 0, 0),
    (1, -2, 2)
]

# 2행 3열 subplot
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

for ax, (a, b, c) in zip(axes.flat, cases):
    # x 범위
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c
    ax.plot(x, y, label=f"{a}x² + {b}x + {c}")
    
    # 축
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)
    
    # 해(근) 표시
    roots = solve_quadratic(a, b, c)
    for r in roots:
        ax.scatter(r, 0, color="red")
        ax.annotate(f"{r:.2f}", (r, 0), xytext=(5, 5), textcoords="offset points", color="red")
    
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend()

plt.suptitle("이차방정식의 그래프와 해 (6가지 경우)", fontsize=18)
plt.tight_layout()
plt.show()
