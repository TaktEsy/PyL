import os
import time

directory = os.getcwd()

for root, dirs, files in os.walk(directory):
    for file in files:
        print(f"Root {root}")

        filepath = os.path.join(root, file)
        filesize = os.path.getsize(filepath)
        filetime = os.path.getmtime(filepath)
        f_filetime =  time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        fileroot = os.path.basename(directory)
        print(f'Обнаружен:{file} Путь: {filepath}, Размер {filesize} байт, Время изменения: {f_filetime}, Корень: {fileroot}')

