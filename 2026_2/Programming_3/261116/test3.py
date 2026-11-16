class Bar:
    def __init__(self):
        self.name = "gsc"

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("exit")

obj = Bar()
with obj as b:
    print(f"{b.name}코드 실행")