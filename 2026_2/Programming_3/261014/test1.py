bar1:list = [2, ] # 타입 힌팅 -> 컬렉션의 종류

bar2:list[float | str] = [2, "2"]
# 타입 힌팅 -> 1) 컬렉션의 종류 2) 원소의 타입

bar3:tuple[int, float, bool] = (2, 3.0, False)
bar4:tuple[float, ...] = (2, 3, 4, 5, 5)
# 타입 힌팅 -> 
# 1) 컬렉션의 종류 
# 2) 원소의 타입
# 3) 각 원소의 타입