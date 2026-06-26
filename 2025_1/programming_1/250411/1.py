def returnNum(argNum):
    print("argNum:", argNum, "\treturnNum() is invoked")
    return argNum

returnNum(1)

#첫 번째 조건: True이므로,
#'returnNum(2) == 2'도 평가되어야 결과를 결정
if True and returnNum(2) == 2:
    print("True")

#첫 번째 조건: False이므로,
#두 번째 조건은 평가되지 않음 -> Lazy expression
if False and returnNum(3) == 2:
    print("True")

#첫 번째 조건: False이므로,
#두 번째 조건은 평가되지 않음 -> Lazy expression
if True or returnNum(4) == 4:
    print("True")

#첫 번째 조건: False이므로,
#두 번째 조건은 평가되지 않음 -> Lazy expression
if False or returnNum(5) == 5:
    print("True")