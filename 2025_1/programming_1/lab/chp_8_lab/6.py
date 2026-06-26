"""
TML 태그 이름과 내용을 매개변수로 받아,
해당 태그로 감싸진 HTML 요소를 반환하는 함수 wrap_in_tag를 작성
"""
# 함수 정의
def wrap_in_tag(char, content):
    # 문서 작성
    total = (f"<{char}>{content}<{char}>")
    # 가져가기
    return total

# 출력: <p>hello<p>
print(wrap_in_tag('p', 'hello'))
# 출력: <b>world<b>
print(wrap_in_tag('b', 'world'))