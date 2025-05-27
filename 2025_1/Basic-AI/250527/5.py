import matplotlib.pyplot as plt

#데이터를 준비
x = range(-10, 11)
y = [val**2 for val in x]

#그래프 종류 선택 후 드로임
plt.scatter(x, y, label="scatter")
plt.bar(x, y, label="bar")

plt.title("A graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)

#그래프 출력
plt.show()