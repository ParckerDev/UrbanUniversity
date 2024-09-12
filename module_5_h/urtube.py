from time import sleep
from user import User
from video import Video


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
            self.current_user = self.users[nickname]
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
            if item.lower() in video.lower():
                result.append(video)
        if result:
            return result
        else:
            print('Не найдено подходящих запросу видео')

    def play_back(self, video: Video):
        for i in range(video.time_now + 1, video.duration + 1):
            print(i, end=' ', flush=True)
            sleep(1)
        print('Конец видео')
            


    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            if title in self.videos:
                video = self.videos[title]
                if not video.adult_mode:
                    self.play_back(video)
                else:
                    if self.current_user.age >= 18:
                        self.play_back(video)
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')


