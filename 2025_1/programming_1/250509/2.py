
foo = [] # list 생성, 요소는 0 개 -> 빈 리스트 생성
pos = list(()) # list 생성, 요소는 0 개 -> 빈 리스트 생성
print(type(foo), type(pos))

foo = [10, 20] # list 생성
pos = list((10, 20)) # list 생성
print(type(foo), type(pos))

foo.append(10)
pos.append(20)
print(foo[0], "\t", pos[0])


foo = [10, 20, 100, 200]
print(len(foo)) # 안에 있는 개수