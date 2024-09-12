from time import sleep


class User:
    def __init__(self, nickname: str, password, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __contains__(self, item):
        return item.lower() in self.title.lower()

class UrTube:
    '''
    user
    '''
    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    def register(self, nickname: str, password, age: int):
        user = User(nickname, password, age)
        if user.nickname not in self.users:
            self.users[user.nickname] = user
            self.login(user.nickname, password)

        else:
            print(f'Пользователь с ником {user.nickname} уже существует! Замените никнэйм')

    def login(self, nickname, password):
        if nickname in self.users and hash(password) == self.users[nickname].password:
            self.current_user = self.users[nickname].nickname
        else:
            print('Несуществующий пользователь или неверный пароль!\nПроверьте вводимые данные!')

    def logout(self):
        self.current_user = None

    def add(self, *args: Video):
        for video in args:
            if video.title not in self.videos:
                self.videos[video.title] = video
            else:
                print(f'Видео с названием "{video.title}" уже есть и не будет загружено!')

    def get_videos(self, item: str):
        result = []
        for video in self.videos:
            if item in video.title:
                result.append(video.title)
        if result:
            return result
        else:
            print('Не найдено подходящих запросу видео')

    def watch_video(self, title):
        if title in self.videos:
            video = self.videos[title]
            if not video.adult_mode:
                for second in range(video.time_now, video.duration):
                    print(second, end=' ')
                    sleep(1)




# TESTS
ut = UrTube()
print(ut.current_user)
ut.register('John Doe', 'password123', 23)
ut.register('Bill', 'password126', 24)
ut.register('Tanya', 'password125', 16)
ut.register('John Doe', '12345pass', 33)
print(ut.users)
print(ut.current_user)

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ut.add(v1, v2)
print(ut.videos)

# Проверка поиска
print(ut.get_videos('лучший'))
print(ut.get_videos('ПРОГ'))
