# 1. 문제 개요
# 사용자로부터 메뉴 번호를 입력받아 
# 해당 도형의 면적을 계산하는 프로그램을 작성한다.

# 2. 문제 설명
# 사용자에게 다음과 같은 메뉴를 보여준다:
#  1. 원의 면적 계산
#  2. 삼각형의 면적 계산
#  3. 사각형의 면적 계산
menu = "1. 원\n2. 삼각형\n3. 사각형"
print("[도형의 면적 계산기]")
print(menu)

# 사용자가 선택한 메뉴 번호에 따라 
user_select = int(input("메뉴를 선택하세요: "))
# 필요한 값을 입력받고 면적을 계산한다.
# if, elif, else 문만을 사용하여 조건을 분기한다.

if user_select == 1:
    radius = float(input("반지름을 입력하세요: "))
    # 원의 면적 = π × 반지름² (π는 3.14로 고정)
    area_circle = radius ** 2 * 3.14
    print(f"원의 면적은 {area_circle}입니다.")
          
elif user_select == 2:
    bowels = float(input("밑변을 입력하세요: "))
    hight = float(input("높이를 입력하세요: "))
    # 삼각형의 면적 = (밑변 × 높이) ÷ 2
    area_triangle = (bowels * hight) / 2
    print(f"삼각형의 면적은 {area_triangle}입니다.")

elif user_select == 3:
    transverse = float(input("가로를 입력하세요: "))
    length = float(input("세로를 입력하세요: "))
    # 사각형의 면적 = 가로 × 세로
    area_rectangle = transverse * length
    print(f"사각형의 면적은 {area_rectangle}입니다.")

else:
    print("잘못된 선택입니다.")