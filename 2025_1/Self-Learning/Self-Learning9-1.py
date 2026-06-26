"""
차량이 어떤 거리를 이동하는 데 걸린 시간과 이동 거리를 바탕으로 평균 속도를 계산
사용자로부터 출발 시간과 도착 시간(시와 분으로 별도 입력), 그리고 이동 거리를 입력
차량의 평균 속도를 km/h 단위로 계산하고, 그 속도가 "느림", "보통", 또는 "빠름"
중 어느 것에 해당하는지 출력
"""
# 입력
start_hour = int(input("출발 시(시간)을 입력하세요: "))
start_minute = int(input("출발 시(분)을 입력하세요: "))
finish_hour = int(input("도착 시(시간)을 입력하세요: "))
finish_minute = int(input("출발 시(분)을 입력하세요: "))
total_far = int(input("이동 거리(km)를 입력하세요: "))

# 계산 정의
def averages():
    total_hour = finish_hour - start_hour
    total_minute = finish_minute - start_minute
    hour_convertion = total_hour * 60
    time_required = total_minute + hour_convertion
    speed_avg = total_far / time_required
    return speed_avg

# 상태
def print_avg():
    if averages() 