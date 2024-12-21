def send_email(mess, rec, sen="university.help@gmail.com"):

    if ("@" in rec and "@" in sen):
        if ".com" in rec or ".ru" in rec or ".net" in rec:
            if ".com" in sen or ".ru" in sen or ".net" in sen:
                if rec == sen:
                    print("Нельзя отправить письмо самому себе!")
                else:
                    if sen == "university.help@gmail.com":
                        print(f"Письмо успешно отправлено с адреса {sen} на адрес {rec}.")
                    else:
                        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sen} на адрес {rec} ")
            else:
                print("Некорректный домен отправителя!")
        else:
            print("Некорректный домен получателя!")
    else:
        print(f"Невозможно отправить письмо с адреса {sen} на адрес {rec}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sen='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sen='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sen='urban.teacher@mail.ru')