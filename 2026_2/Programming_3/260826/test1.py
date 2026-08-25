class Student:
    def __init__(self, name):
        self.name = name  # ← これはオブジェクトごとに個別

    def greet(self):
        print(f"{self.name}です")  # ← 処理内容は共通、selfの中身だけ違う

std1 = Student("田中")
std2 = Student("鈴木")
std1.greet()  # 田中です
std2.greet()  # 鈴木です