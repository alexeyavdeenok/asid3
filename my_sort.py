import random
import matplotlib.pyplot as plt
import time
from functools import wraps


def visualize_sort(func):
    @wraps(func)
    def wrapper(arr, *args, visualize=False, **kwargs):
        # Если визуализация отключена, просто вызываем исходную функцию
        if not visualize:
            return func(arr, *args, **kwargs)

        fig, ax = plt.subplots()
        bars = ax.bar(range(len(arr)), arr, color='grey')
        plt.ion()  # Включаем интерактивный режим

        def update_bars(array, color_indices=None):
            for idx, bar in enumerate(bars):
                bar.set_height(array[idx])
                if color_indices and idx in color_indices:
                    bar.set_color('red')  # Подсвечиваем текущие элементы
                else:
                    bar.set_color('grey')
            if 25 <= len(array) < 50:
                plt.pause(0.01)  # Пауза для анимации
            elif len(array) < 25:
                plt.pause(0.1)
            else:
                plt.pause(0.001)
            fig.canvas.draw()

        def visualize_swap(i, j):
            update_bars(arr, color_indices=[i, j])  # Обновляем бары
            time.sleep(0)  # Задержка для визуализации обмена

        # Внедряем визуализацию в функцию сортировки
        kwargs['visualize_swap'] = visualize_swap

        result = func(arr, *args, **kwargs)

        update_bars(arr)  # Финальное обновление
        plt.ioff()  # Выключаем интерактивный режим
        plt.show()  # Показываем финальный график
        return result

    return wrapper


@visualize_sort
def my_sort(array, reverse=False, key=lambda x: x, cmp=None, visualize_swap=None):
    if cmp is None and not reverse:
        def cmp(x, y):
            x_keyed = key(x)
            y_keyed = key(y)
            if x_keyed < y_keyed:
                return -1
            elif x_keyed > y_keyed:
                return 1
            else:
                return 0
    elif cmp is None and reverse:
        def cmp(x, y):
            x_keyed = key(x)
            y_keyed = key(y)
            if x_keyed > y_keyed:
                return -1
            elif x_keyed < y_keyed:
                return 1
            else:
                return 0

    sort_list(array, key, cmp, 0, len(array) - 1, visualize_swap)
    return array


def sort_list(array, key, cmp, first, last, visualize_swap):
    if first >= last:
        return
    else:
        q = random.choice(array[first:last + 1])  # Опорный элемент
        i = first
        j = last
        while i <= j:
            while cmp(array[i], q) < 0:
                i += 1
            while cmp(array[j], q) > 0:
                j -= 1
            if i <= j:
                if visualize_swap:
                    visualize_swap(i, j)  # Визуализируем обмен
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        sort_list(array, key, cmp, first, j, visualize_swap)
        sort_list(array, key, cmp, i, last, visualize_swap)


# Пример использования
if __name__ == "__main__":
    array1 = [_ for _ in range(200)]
    random.shuffle(array1)  # Перемешиваем массив
    print("Исходный массив:", array1)

    # Вызов с визуализацией
    sorted_array_with_visualize = my_sort(array1, reverse=True, visualize=True)
    print("Отсортированный массив (с визуализацией):", sorted_array_with_visualize)


