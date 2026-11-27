class Bar:
    @classmethod # <- decorator
    def prt_somthing(cls, msg:str) -> str:
        return f"안녕하세요 {msg}"