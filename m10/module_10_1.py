import time
from time import sleep
from threading import Thread

# Объявление функции write_words
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding="UTF-8") as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

# Измерение времени выполнения функций
start_time = time.time()

# Последовательный вызов функции
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

end_time = time.time()
print("Работа последовательного вызова:", end_time - start_time)

# Создание потоков
start_time_threads = time.time()

threads = [
    Thread(target=write_words, args=(10, "example5.txt")),
    Thread(target=write_words, args=(30, "example6.txt")),
    Thread(target=write_words, args=(200, "example7.txt")),
    Thread(target=write_words, args=(100, "example8.txt"))
]

# Запуск потоков
for thread in threads:
    thread.start()

# Ожидание завершения потоков
for thread in threads:
    thread.join()

end_time_threads = time.time()
print("Работа потоков:", end_time_threads - start_time_threads)
