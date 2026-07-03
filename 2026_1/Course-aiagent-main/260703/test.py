import time

def make_order(menu:str, taken_time:int)->str:
    print(f"{menu} 준비중")
    time.sleep(taken_time)
    return f"{menu} 준비 완료"

def main():
    start = time.time()
    print(make_order("라떼", 3))
    print(make_order("아아", 2))
    print(make_order("우유", 1))

    elasped_time = time.time() - start

    print(f"경과 시간 {elasped_time}")

if __name__ == "__main__":
    main()