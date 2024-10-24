import random
import matplotlib.pyplot as plt


# Главная функция сортировки
def my_sort(array, reverse=False, key=lambda x: x, cmp=None):
    if cmp is None:
        def cmp(x, y):
            x_keyed = key(x)
            y_keyed = key(y)
            if x_keyed < y_keyed:
                return -1
            elif x_keyed > y_keyed:
                return 1
            else:
                return 0

    # Создание визуализации
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(array)), array, color='blue')
    ax.set_title("Sorting Visualization")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")

    # Передаем массив и ось для обновления в функции сортировки
    sort_list(array, key, cmp, 0, len(array) - 1, bars, ax)

    if reverse:
        return array[::-1]
    return array


# Функция сортировки с визуализацией
def sort_list(array, key, cmp, first, last, bars, ax):
    if first >= last:
        return
    else:
        # Используем среднее значение для разбиения
        average = random.choice(array[first:last + 1])
        i = first
        j = last
        while i <= j:
            while i <= last and array[i] < average:
                i += 1
            while j >= first and array[j] > average:
                j -= 1
            if i <= j:
                # Обмен элементов
                array[i], array[j] = array[j], array[i]

                # Обновление графика
                update_bars(bars, array)

                i += 1
                j -= 1

        sort_list(array, key, cmp, first, j, bars, ax)
        sort_list(array, key, cmp, i, last, bars, ax)


# Функция обновления графика
def update_bars(bars, array):
    for bar, height in zip(bars, array):
        bar.set_height(height)
    plt.pause(0.001)  # Уменьшена задержка для ускорения анимации


# Пример использования
if __name__ == "__main__":
    random_array = [_ for _ in range(100)]  # Генерация случайного массива
    random.shuffle(random_array)
    print("Исходный массив:", random_array)
    sorted_array = my_sort(random_array)
    print("Отсортированный массив:", sorted_array)
    plt.show()  # Показать график
