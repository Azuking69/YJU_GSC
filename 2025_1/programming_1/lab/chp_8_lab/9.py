"""
학생의 이름과 여러 과목의 점수를 입력받아, 총 점수를 계산하는 함수를 작성
"""
#1 함수 작성
def student_score(name, **scores):
    print(f"{name}의 성적:")

    total = 0
    for subject, score in scores.items():
        print(f"- {subject}: {score}점")
        total += score
    
    print(f"총점: {total}점")

# 성적
student_score("민수", math=90, english=85, science=88)