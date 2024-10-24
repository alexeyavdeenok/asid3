
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

@log_execution_time
def print_result(num):
    print(my_sort(num))

print_result([random.randint(-100, 100) for _ in range(100)])