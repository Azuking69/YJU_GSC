"""
별다방에서 고객의 주문을 받아 음료 가격과 혜택을 계산하는 프로그램
이 실습문제를 통해 선택문 흐름 제어의 다양한 구조를 이해
실제 서비스 로직 설계에 가까운 조건문 분기를 실습
"""

#1 주문 입력
user_select_menu = input("음료를 입력하세요(coffee/latte/juice): ")
user_select_size = input("크기를 선택하세요(small/medium/large): ")
#멤버십 여부
member_ship = input("멤버십이신가요?(yes/no): ")
#행을 바꿈
print()

#2 가격 정의
#coffe 3000원
menu_price = 3000
#latte 4000원
if user_select_menu == "latte":
    menu_price = 4000
#juice 3500원
elif user_select_menu == "juice":
    menu_price = 3500

#3 크기 추가 가격 정의
#small 0원
size_price = 0
#medium 500원
if user_select_size == "medium":
    size_price = 500
#large 1000원
else:
    size_price = 1000


#6 출력
#선택 메뉴 가격
print(f"기본 가격: {menu_price}원")
#크기 가격
print(f"크기 추가 요금: {size_price}원")
#할인 정의
#멤버십 있음
if member_ship == "yes":
    service_price = int((menu_price + size_price) * 10 / 100)
    print(f"할인 적용: -{service_price}")
#멤버십 없음
else:
    service_price = 0
    print(f"할인 적용: 없음")
#결과
print(f"최종 결제 금액: {int(menu_price + size_price - service_price)}원")
#멤버십 셧 추가
if user_select_menu in ["coffee", "latte"] and member_ship == "yes" and user_select_size == "large":
    print("무료 샷이 제공됩니다!")