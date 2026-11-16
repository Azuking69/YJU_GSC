class Bar:
    def __init__(self, file_name):
        self._file_name = open(file_name, 'r', encoding='utf-8')

    def __iter__(self):
        yield from self._file_name

obj = Bar("gsc.txt")

for text in obj:
    print(text)