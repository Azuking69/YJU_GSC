"""
위치 인자 + 기본값이 있는 키워드 인자 혼합
상품명과 가격을 위치 인자로 받고, 부가세율은 키워드 인자로 받도록 하여
최종 가격을 계산하는 함수를 작성
부가세율은 입력하지 않으면 기본적으로 10%가 적용되며, 
필요 시 tax=0.08처럼 옵션으로 조정할 수 있다
"""
def calc_price(product, price, tax=0.10):
    total_tax = price * tax
    total_price = price + total_tax
    print(f"{product}: {int(total_price)}원")


# 출력: 노트북의 최종 가격은 1,100,000원
calc_price("노트북", 1000000)
# 출력: 모니터의 최종 가격은 315,000원
calc_price("모니터", 300000, tax=0.05)