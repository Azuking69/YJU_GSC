"""
고객의 기본 정보, 관심 항목, 기타 메타 정보를 바탕으로 
개인 맞춤형 요약 보고서를 생성하는 함수를 작성
"""
# 함수 요구사항
def gererate_profile(name, age, gender="미정", *interests, **metadata):
    print(f"""[고객 프로필]
이름: {name}
나이: {age}
성별: {gender}""")
    
    # 고객이 선택한 관심 항목
    if interests:
        print(f"관심사: {',' .join(interests)}")
    
    # 기타 추가 정보
    if metadata:
       extra_info = ", ".join(f"{key}={value}" for key, value in metadata.items())
       print(f"추가 정보: {extra_info}")

# 고객 정보1
gererate_profile("홍길동", 30)

#고객 정보2
gererate_profile("지민", 26, "여성", *["여행", "사진", "독서"], job="디자이너", country="한국")