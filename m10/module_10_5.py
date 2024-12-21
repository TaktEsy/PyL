import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

if __name__ == '__main__':
    # Создаем список файлов
    filenames = [f'./res/file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.perf_counter()
    for filename in filenames:
        read_info(filename)
    end_time = time.perf_counter()
    print(f"Линейный вызов: {end_time - start_time:.6f} секунд")

    # Многопроцессный вызов
    start_time = time.perf_counter()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.perf_counter()
    print(f"Многопроцессный вызов: {end_time - start_time:.6f} секунд")
