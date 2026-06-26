# list -> object, []=list 생성
bar = [50, 10, 30, 40, 20] # 요소(Element)
# bar = 변수

for index in range(5):
    print(bar[index], end="\t")

bar[0] = 200
bar[4] = 100

print(bar)