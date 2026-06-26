"""
슬라이싱을 활용한 리스트 분할 및 메뉴 기반 데이터 관리
"""
import random

# 메뉴 작성
menu = """
=== 리스트 관리 프로그램 ===
1. 각 리스트 내 데이터 출력
2. 특정 리스트 출력
3. 특정 리스트 삭제
4. 프로그램 종료
메뉴 선택: """

# 난수 저장되는 리스트 작성 
num_list = []
# 난수 20개를 생성
for _ in range(20):
    random_val = random.randint(0, 100)
    num_list.append(random_val)
# 생성 확인
print(f"이번에 난수: {num_list}")    


count5_list = num_list
for i in range(4):
    val_list = []
    val_list += count5_list[::4]
    count5_list.pop([::4])
    print(val_list)


# 반복적으로 메뉴 출력
while True:
    # 사용자로부터 메뉴 입력 받는다
    input_menu = int(input(menu))
    
    #1. 각 리스트 내 데이터 출력
    if input_menu == 1:
        for j in range(4):
            print(f"[리스트 {j}]: {val_list}")
        
    
    #2. 특정 리스트 출력
    elif input_menu == 2:
        # 사용자로부터 출력할 리스트 번호 입력 받는다
        input_ID = int(input("출력할 리스트 번호 입력: "))
        # 데이터가 없을 때
        if input_ID not in val_list:
            print("해당 번호 리스트가 없습니다.")
        else:
            print(f"리스트 {input_ID} : {val_list[input_ID]}")
    
    #3. 특정 리스트 삭제
    elif input_menu == 3:
        # 사용자로부터 삭제할 리스트 번호 입력 받는다
        input_ID = int(input("삭제할 리스트 번호 입력: "))
        # 데이터가 없을 때
        if input_ID not in val_list:
            print("해당 번호 리스트가 없습니다.")
        else:
            # 삭제
            del val_list[input_ID]
            # 완료 알림
            print("삭제가 되었습니다.")
    
    #4. 프로그램 종료
    elif input_menu == 4:
        print("프로그램을 종료합니다.")
    
    # 예외 처리
    else:
        print("잘못된 입력입니다. 1~4의 사이 숫자를 입력하세요.")
