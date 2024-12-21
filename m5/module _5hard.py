import hashlib
class UrTube():

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        for user in self.users:
            if user["nickname"] == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = {"nickname": nickname, "password": hash(password), "age": age}
        self.users.append(new_user)
        print(f"Пользователь {nickname} успешно зарегистрирован")
        self.log_in(nickname, password)

        # for user in self.users:
        #     print(user)
        #     if user['nickname'] == nickname:
        #     else:
        #         new_user = {
        #             'nickname': nickname,
        #             'password': password,
        #             'age': age
        #         }
        #         self.users.append(new_user)
        #
        #         # автоматический вход после регистрации
        #         self.log_in(nickname, password)

    def log_in(self, nickname, password):
        for user in self.users:
            if user['nickname'] == nickname and user['password'] == hash(password):
                self.current_user = user
                return print(f'Добро пожаловать ', nickname)

        print('Неверные логин или пароль!')


    def log_out(self):
        n=self.current_user["nickname"]
        print(f'До свидания, {n}')
        self.current_user = None
        return

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word = search_word.lower()
        result = []

        for video in self.videos:

            if search_word in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, video_title):
        for video in self.videos:
            if video_title in video.title:

                if self.current_user == None:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                    return
                elif self.current_user["age"] < 18:
                    print("Вам нет 18!")
                    return

                print("Воспроизводится видео:")
                print(video.title)

                for s in range(1, video.duration+1):
                    print(f"Секунда: {s}")
                print("Конец видео.")

class User():
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.__hash__(password)
        self.age = age

        def _hash_password(self, password):
            # Хэшируем пароль с помощью SHA-256
            return int(hashlib.sha256(password.encode()).hexdigest(), 16)

class Video():

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

print("===============================")
print("Добавление видео: ")
ur.add(v1, v2)

print("===============================")
print("Поиск: ")
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

print("===============================")
print("Регистрация: ")
ur.register('lexa2010', '2010lexa', 14)
ur.register('urban', 'hash512', 30)
print(f"Все юзеры: {ur.users}")

print("===============================")
print("Вход: ")
ur.log_in('urban', 'hash512')
print(f"Текущий юзер: {ur.current_user}")
# ur.log_out()
# print(f"Текущий юзер: {ur.current_user}")

print("===============================")
print("Воспроизведение: ")
print(f"Текущий юзер: {ur.current_user}")
ur.watch_video('Лучший язык программирования 2024 года')

print()




