class User:
    def __init__(self, nickname: str, password, age: int):
        self.nickname = nickname
        password = hash(password)
        age = age