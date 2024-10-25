# def partition(nums, low, high):
#     # Выбираем средний элемент в качестве опорного
#     # Также возможен выбор первого, последнего
#     # или произвольного элементов в качестве опорного
#     pivot = nums[(low + high) // 2]
#     i = low - 1
#     j = high + 1
#     while True:
#         i += 1
#         while nums[i] < pivot:
#             i += 1
#
#         j -= 1
#         while nums[j] > pivot:
#             j -= 1
#
#         if i >= j:
#             return j
#
#         # Если элемент с индексом i (слева от опорного) больше, чем
#         # элемент с индексом j (справа от опорного), меняем их местами
#         nums[i], nums[j] = nums[j], nums[i]
#
# def quick_sort(nums):
#     # Создадим вспомогательную функцию, которая вызывается рекурсивно
#     def _quick_sort(items, low, high):
#         if low < high:
#             # This is the index after the pivot, where our lists are split
#             split_index = partition(items, low, high)
#             _quick_sort(items, low, split_index)
#             _quick_sort(items, split_index + 1, high)
#
#     _quick_sort(nums, 0, len(nums) - 1)
#
# # Проверяем, что оно работает
# random_list_of_nums = [22, 5, 1, 18, 99]
# quick_sort(random_list_of_nums)
# print(random_list_of_nums)
#
# def QuickSort(A, l, r):
#     if l >= r:
#         return
#     else:
#         q = random.choice(A[l:r + 1])
#         i = l
#         j = r
#         while i <= j:
#             while A[i] < q:
#                 i += 1
#             while A[j] > q:
#                 j -= 1
#             if i <= j:
#                 A[i], A[j] = A[j], A[i]
#                 i += 1
#                 j -= 1
#                 QuickSort(A, l, j)
#                 QuickSort(A, i, r)

# import matplotlib.pyplot as plt
#
# # Данные для визуализации
# data = [
#     1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#     21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40
# ]
# colors = ['red' if i == 0 else 'lightgray' for i in range(len(data))]
# values = [5, 15, 10, 5, 20, 12, 18, 16, 25, 15, 22, 18, 14, 10, 8, 12, 16, 14, 10, 18, 20, 16, 22, 12, 10, 18, 14, 10, 16, 14, 10, 12, 10, 14, 12, 10, 14, 12, 10, 8]
#
# # Создание графика
# plt.bar(data, values, color=colors)
#
# # Настройка графика
# plt.xticks([])
# plt.yticks([])
# plt.axis('off')
#
# # Отображение графика
# plt.show()
def encode_string(s):
    """Кодирует строку в числовое значение для алфавитной сортировки."""
    # Кодируем строку в число, основанное на ASCII-кодах символов с весом для каждой позиции
    base = 128  # База для возведения в степень (например, ASCII-таблица 0-127)
    encoded_value = sum(ord(char) * (base ** i) for i, char in enumerate(s))
    return encoded_value

def decode_number(encoded_value, original_strings):
    """Декодирует числовое значение обратно в строку, используя список оригинальных строк."""
    # Создаем словарь для быстрого поиска строки по закодированному значению
    encoding_map = {encode_string(s): s for s in original_strings}
    return encoding_map.get(encoded_value, None)

# Пример использования
strings = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Кодируем строки в числовые значения
encoded_strings = [(encode_string(s), s) for s in strings]

# Сортируем по числовым значениям
encoded_strings.sort()

# Извлекаем строки в отсортированном алфавитном порядке
sorted_strings = [decode_number(val, strings) for val, _ in encoded_strings]

print("Закодированные значения:", [val for val, _ in encoded_strings])
print("Отсортированные строки:", sorted_strings)