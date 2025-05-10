score = [99, 29, 30, 40, 20, 60]

student_num = len(score)

sum = 0

for s in score:
    sum += s


avg = sum / student_num

print("학생 수:", student_num, "총점 : ", sum, "평균 : ", avg)