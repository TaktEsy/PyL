class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username

        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    db = Database()

    while True:
        choice = int(input('Выберите действие: \n1 - Вход\n2 - Регистрация\n'))
        if choice == 1:
            login = input("Логин: ")
            password = input("Пароль: ")
            if login in db.data:
                if password == db.data[login]:
                    print(f"Добро пожаловать, {login}")
                    break
                else:
                    print("Пароль неверный!")
            else:
                print("Пользователь не найден!")
        elif choice == 2:
            user = User(input("Login: "), password := input("Password: "),
                        password_confirm := input("Repeat password: "))

            if password != password_confirm:
                exit('Пароли не совпадают!')
            elif len(password) < 2:
                exit('Символов должно быть больше!')
            else:
                counter = 0
                for s in password:
                    if s.isupper():
                        counter += 1
                if counter == 0:
                    exit('Нет заглавной!')
            db.add_user(user.username, user.password)

        print(db.data)