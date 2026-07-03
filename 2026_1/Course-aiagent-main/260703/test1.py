import asyncio


async def main():
    print("hello world")

def test():
    print("안녕 세상아~")

if __name__ == "__main__":
    test() # 동기 함수
    print(type(main()))