"""
사용자 입력을 통해 리스트의 요소를 추가(Create), 조회(Read), 수정(Update),
삭제(Delete)하는 기능
"""
import sys

#1 빈 리스트 items를 생성
new_list = []

#2  사용자에게 다음 중 하나의 작업을 선택하게 한다
menu = """
1: 요소 추가 (Create)
2: 요소 조회 (Read)
3: 요소 수정 (Update)
4: 요소 삭제 (Delete)
5: 종료 (Exit)"""

#3 사용자는 작업 번호를 계속 입력할 수 있으며, 5번을 입력하면 종료한다.
count = 0
while True:
    user_input = int(input(f"""작업을 선택하세요: {menu}
입력: """))

    if 6 <= user_input:
        print("올마른 번호를 입력하세요\n")

    elif user_input == 5:
        print("프로그램을 종료함니다.")
        sys.exit()

    #4 사용자로부터 문자열을 입력받아 리스트의 끝에 추가
    elif user_input == 1:
        user_num = int(input("추가할 값을 입력하세요: "))
        new_list.append(user_num)
        print("추가 완료.")
        count += 1
    
    #5 현재 리스트의 모든 요소를 인덱스와 함께 출력
    elif user_input == 2:
        print("[현재 리스트 내용]")
        for i in range(count):
            print(f"{i} : {new_list[i]}")
    
    #6 인덱스와 새로운 값을 입력받아 해당 인덱스의 요소를 수정
    elif user_input == 3:
        update_index = int(input("수정할 인덱스를 입력하세요: "))
        #7 인덱스가 잘못되었을 경우 안내 메시지를 출력
        if count < update_index:
            print("유호하지 않은 인덱스입니다.")
        else:
            update_num = int(input("새로운 값을 입력하세요: "))
            new_list[update_index] = update_num
            print("수정 완료.\n")
    
    #8 인덱스를 입력받아 해당 위치의 요소를 삭제
    else:
        delete_index = int(input("삭제할 인덱스를 입력하세요: "))
        if count < delete_index:
            print("유호하지 않은 인덱스입니다.")
        else:
            del new_list[delete_index]
            print("삭제 완료.\n")
            count -= 1 