import time

def main():
    start = time.time()
    time.sleep(2) # 2초 정지
    elasped_time = time.time() - start

    print(f"경과 시간 {elasped_time}")

if __name__ == "__main__":
    main()