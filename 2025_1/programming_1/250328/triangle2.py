#정사각형의 면적을 구하세요

#가로 또는 세로의 길이가 0 또는 음수일 경우
#->"양수를 입력하세요"출력 후 종료

size_of_rect = int(input("가로 또는 세로의 길이:"))
if size_of_rect <= 0:
    print("양수를 입력하세요")
    
else:
    print(size_of_rect**2)