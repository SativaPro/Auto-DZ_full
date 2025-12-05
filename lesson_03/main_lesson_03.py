# запуск всех заданий

import sys
import os
sys.dont_write_bytecode = True #чтобы не кешировать при запуске

# Получаем путь к текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

print("*** Задание 1 ***")
sys.path.insert(0, current_dir)  # Добавлят текущую папку в путь поиска модулей
from lesson_3_task_1 import *    # Импортир содержимого из файла

print("*** Задание 2 ***")
from lesson_3_task_2 import *

print("*** Задание 3 ***")
from lesson_3_task_3 import *
