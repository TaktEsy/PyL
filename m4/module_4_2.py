def test_func():
    def in_func():
        print("Я в области видимости функции test_function")

    in_func()

# Будет ошибка
# in_func()
test_func()
