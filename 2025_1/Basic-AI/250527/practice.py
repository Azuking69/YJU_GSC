import matplotlib.pyplot as plt

# data 준비
x = range(-10, 11)
y1 = x
y2 = [3*val for val in x]
y3 = [val**2 for val in x]

#그래프 종류 선택 후 드로임
plt.plot(x, y1, label="x1", color="blue")
plt.plot(x, y2, label="x2", color="red")
plt.plot(x, y3, label="x3", color="orange")

plt.title("Graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

#출력
plt.show()