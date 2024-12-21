class User:
    def __init__(self, nickname, password, age):
        self.data = {'Login':[hash("password"), age]}
        self.data=age
        # self.data[nickname] = password
        self.nickname = nickname
        self.password = password
        self.age = age
class Video:
    videos = []

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

        self.videos.append([title, duration])


        print(self.videos)

class UrTube(Video):

    videos = Video.videos
    cuser = []

    def __init__(self):
         pass

    def log_in(self, nickname, password):
        """
        Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем.
        Если такой пользователь существует, то current_user меняется на найденного.
        Помните, что password передаётся в виде строки, а сравнивается по хэшу.
        :param nickname:
        :param password:
        :return:
        """
    def register(self, nickname, password, age):
        """
        Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
        если пользователя не существует (с таким же nickname). Если существует, выводит на экран:
        "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически.
        :param nickname:
        :param password:
        :param age:
        :return:
        """
        pass

    def log_out(self):
        pass

    def add(self, *args):
        pass
    def get_videos(self, found):
        pass

    def watch_video(self):
        pass

class Test:
    def test(self, v):
        self.v = v
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=18)
