#주어진 점수 리스트에서 각 학기별 최고 점수를 찾아 출력

#주어진 점수 리스트는 두 학기의 점수를 연속해서 포함
score = [88, 92, 75, 65, 79, 84, 91, 87, 90, 88]

#スコアの合計数の半分のところでスライシングする
half = len(score) // 2

first_score = score[:half]
second_score = score[half:]

#결과 출력
print(f"1학기 최고 점수:{max(first_score)}")
print(f"2학기 최고 점수:{max(second_score)}")
