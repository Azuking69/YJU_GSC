import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

#한국어 폰트
font_path = "C:/Windows/Fonts/malgun.ttf"
fontprop = fm.FontProperties(fname=font_path)

#값
x = [val for val in range(0, 20 + 1)]
y = [val ** 2 for val in x]
print(x)
print(y)

#그래프 종류 선택
plt.plot(x, y, color='red', marker="*") #선형 그래프

#그래프 꾸미기
plt.xlabel("X 축", fontproperties=fontprop)
plt.ylabel("Y 축", fontproperties=fontprop)
plt.title("선형 그래프", fontproperties=fontprop)
plt.grid(True)

#그래프 출력
plt.show()