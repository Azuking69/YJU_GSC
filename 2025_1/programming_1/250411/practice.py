"""
고객의 쇼핑 데이터를 기반으로 분석을 수행한 후, 위험 고객, 우수 고객, 일반 고객중
하나로 고객 등급을 판별
"""

import sys

# 사용자로부터 다음 값을 입력받는다
total_bought_price = int(input("총 구매 금액: "))#구매 금액 (정수형)
return_count = int(input("총 반품 횟수: "))#반품 횟수 (정수형)
bought_count = int(input("총 구매 횟수: "))#구매 횟수 (정수형)
signup_month = int(input("가입 개월 수: "))#가입 개월 수 (정수형)
if bought_count <= 0:
    print("오류: 구매 회수가 0입니다. 반품률을 계산할 수 없습니다.")
    sys.exit()
elif return_count > bought_count:
    print("오류: 반품 횟수가 구매 횟수보다 많을 수 없습니다.")
    sys.exit()


# 고객 등급 분류 기준
# 위험 고객 판별 → 우수 고객 판별 → 일반 고객 분류
return_percent = return_count / bought_count * 100 # 반품률 계산
def denger_costmer():
    if return_percent >= 50 or signup_month <= 3 or total_bought_price <= 10000 or return_count >= 10:
       return '위험 고객'
    elif total_bought_price >= 2000000 and return_percent <= 10.00 and bought_count >= 30:
       return '우수 고객'
    else:
       return '일반 고객'


# 출력
denger_costmer = denger_costmer()
# 반품률 출력
print(f"\n반품률: {return_percent:.1f}%")
# 판별된 고객 분류 결과 출력
print(f"결과: {denger_costmer}")