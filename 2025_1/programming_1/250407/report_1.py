"""
사용자가 입력한 상품 가격에 따라 할인율을
적용하여 할인 금액과 최종 결제 금액을 계산하는 프로그램
"""

#1 사용자가 구매한 상품 가격을 입력
user_price = int(input("상품 가격을 입력하세요: "))

#2 조건에 따라 할인율 결정
if user_price >= 100000:
    discount_percent = 10
    print(f"할인율: {discount_percent}%")
    #2-1 할인 금액 = 상품 가격 × 할인율 (%)
    discount_price = user_price * (discount_percent / 100)

elif user_price >= 50000:
    discount_percent = 5
    print(f"할인율: {discount_percent}%")
    #2-1 할인 금액 = 상품 가격 × 할인율 (%)
    discount_price = user_price * (discount_percent / 100)
#2-2 5만 원 미만 구매 시 할인 없음
else:
    discount_percent = user_price
    print(f"할인율: 0%")

#2-2 최종 결제 금액 = 상품 가격 - 할인 금액
print(f"할인 금액: {int(discount_price)}원")

#3  할인율, 할인 금액, 최종 결제 금액 출력
print(f"최종 결제 금액: {int(user_price- discount_price)}원")