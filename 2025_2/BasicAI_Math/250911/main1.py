import numpy as np
import matplotlib.pyplot as plt

# 利益関数 y = -2x^2 + 12x - 10
def profit(x):
    return -2*x**2 + 12*x - 10

# x の範囲（0～6百万円くらい）
x = np.linspace(0, 6, 200)
y = profit(x)

# グラフ作成
plt.figure(figsize=(8,6))
plt.plot(x, y, label="y = -2x² + 12x - 10", color="orange")

# 軸
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

# 頂点 (3, 8)
plt.scatter(3, 8, color="red")
plt.annotate("(3, 8)", (3, 8), xytext=(10, 10), textcoords="offset points", color="red")

plt.title("広告費と利益の関係")
plt.xlabel("広告費 (百万円)")
plt.ylabel("利益 (百万円)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
