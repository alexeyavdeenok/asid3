import pygame
import random
import time

# Константы для визуализации
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Максимальное количество элементов для визуализации
MAX_ELEMENTS = 300

# Инициализация Pygame
pygame.init()


# Функция для масштабирования значений массива в диапазон для визуализации
def scale_array(array, max_height=SCREEN_HEIGHT):
    max_val = max(array)
    min_val = min(array)
    scale_factor = (max_height - 50) / (max_val - min_val) if max_val != min_val else 1
    return [(val - min_val) * scale_factor for val in array]


# Функция для отображения списка в виде столбцов
def draw_bars(screen, array, bar_width, color_positions=None):
    screen.fill(WHITE)
    for i, val in enumerate(array):
        color = RED if color_positions and i in color_positions else BLUE
        pygame.draw.rect(screen, color, (i * bar_width, SCREEN_HEIGHT - val, bar_width - 1, val))
    pygame.display.flip()


# Декоратор для визуализации сортировки
def visualize_sort(func):
    def wrapper(array, *args, visualize=False, **kwargs):
        if not visualize:
            return func(array, *args, **kwargs)

        num_elements = len(array)

        # Ограничение на количество элементов для визуализации
        if num_elements > MAX_ELEMENTS:
            scale_factor = num_elements / MAX_ELEMENTS
            array = [int(val / scale_factor) for val in array]  # Масштабируем значения
            num_elements = MAX_ELEMENTS

        # Инициализация экрана для визуализации
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Quick Sort Visualization")

        # Масштабируем массив для визуализации
        scaled_array = scale_array(array, SCREEN_HEIGHT)

        # Определяем ширину столбцов на основе количества элементов
        bar_width = max(1, SCREEN_WIDTH // num_elements)

        # Основной цикл Pygame для визуализации
        def visualize_swap(i, j):
            draw_bars(screen, scaled_array, bar_width, color_positions=[i, j])
            # Уменьшаем задержку в зависимости от количества элементов
            delay = max(0.05, 2.0 / num_elements)  # Задержка не менее 0.01 секунды
            time.sleep(delay)

        kwargs['visualize_swap'] = visualize_swap
        func(scaled_array, *args, **kwargs)

        # Отображаем отсортированный массив
        draw_bars(screen, scaled_array, bar_width)

        # Ожидание закрытия окна пользователем
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()

    return wrapper


@visualize_sort
def my_sort(array, reverse=False, key=lambda x: x, cmp=None, visualize_swap=None):
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

    sort_list(array, key, cmp, 0, len(array) - 1, visualize_swap)

    if reverse:
        array.reverse()  # Изменяем сам массив на месте
    return array


# Реализация быстрой сортировки с визуализацией
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
                # Визуализируем обмен элементов
                if visualize_swap:
                    visualize_swap(i, j)
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        sort_list(array, key, cmp, first, j, visualize_swap)
        sort_list(array, key, cmp, i, last, visualize_swap)


# Пример использования
if __name__ == "__main__":
    # Задаем количество элементов в массиве
    num_elements = 300# Изменяйте количество элементов как вам нужно
    array = [_ for _ in range(num_elements)]  # Генерация массива
    random.shuffle(array)
    my_sort(array, visualize=True)

    # Запуск сортировки без визуализации
    # my_sort(array, visualize=False
