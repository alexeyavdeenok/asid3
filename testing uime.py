
from my_sort import my_sort
import random
import time


# Декоратор для логирования времени выполнения
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Начало времени выполнения
        result = func(*args, **kwargs)
        end_time = time.time()  # Окончание времени выполнения
        execution_time = end_time - start_time  # Вычисляем время выполнения

        # Вывод в консоль
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")

        return result

    return wrapper


def bubble_sort(array, reverse=False, key=None, cmp=None):
    # Используем стандартный ключ, если он не задан
    if key is None:
        key = lambda x: x

    # Устанавливаем компаратор по умолчанию, если он не задан
    if cmp is None:
        cmp = lambda x, y: (key(x) > key(y)) - (key(x) < key(y))

    n = len(array)

    for i in range(n):
        swapped = False  # Флаг для оптимизации
        for j in range(0, n - i - 1):
            # Определяем направление сортировки
            if (cmp(array[j], array[j + 1]) > 0 and not reverse) or \
                    (cmp(array[j], array[j + 1]) < 0 and reverse):
                # Меняем местами, если элементы не в порядке
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True  # Помечаем, что был обмен
        # Если не было обменов, то массив уже отсортирован
        if not swapped:
            break

    return array




@log_execution_time
def print_result(arr, flag):
    if flag == 1:
        print(my_sort(arr))
    else:
        print(bubble_sort(arr))


array1 = [i for i in range(2000)]
random.shuffle(array1)
array2 = array1.copy()
print_result(array1, 1)
print_result(array2, 2)