# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

file_path1 = str(os.path.abspath('test_file.txt'))
file_path2 = "C:\\IT\GeekBrains\\Python\\homeworks\\lesson5\\test_file.txt"


def file_location_splition1(file_path):
    way = os.path.split(file_path)[0]
    base_name = os.path.basename(file_path)
    file_name, file_extention = os.path.splitext(base_name)
    return way, file_name, file_extention


print(file_location_splition1(file_path2))          # Вводим путь в виде строки
print(file_location_splition1(file_path1))          # Вводим путь через указание файла
