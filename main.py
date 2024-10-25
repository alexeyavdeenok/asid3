import argparse
import random
import os
from my_sort import my_sort


def create_parser():
    """
    Создает парсер для аргументов командной строки.
    :return: объект parser
    """
    parser = argparse.ArgumentParser(description='Обработка массива с различными функциями.')

    parser.add_argument('-wl', '--write_list', nargs='+', type=str,
                        help='Ввод элементов массива через пробел')
    parser.add_argument('-t', '--type', choices=['str', 'int'], default='int',
                        help='Тип элементов массива (по умолчанию: int)')
    parser.add_argument('-gr', '--generate_random', nargs=3, type=int,
                        help='Генерация массива заполненного случайными значениями: '
                             'минимальное число, максимальное число, количество чисел')
    parser.add_argument('-gs', '--generate_shuffle', type=int,
                        help='Случайная перестановка n элементов')
    parser.add_argument('-v', '--visualize', action='store_true', default=False,
                        help='Визуализация алгоритма (по умолчанию: False)')
    parser.add_argument('-r', '--readfile', type=str,
                        help='Чтение файла, получает путь к файлу')
    parser.add_argument('-w', '--writefile', type=str,
                        help='Запись массива в файл, получает путь для записи')
    parser.add_argument('-rev', '--reverse', action='store_true', default=False,
                        help='Сортировка по убыванию (по умолчанию: False)')

    return parser


def generate_list_from_input(input_string, element_type):
    """Создает массив из строки ввода в зависимости от типа элементов."""
    if element_type == 'int':
        return list(map(int, input_string))
    return input_string


def generate_random_list(min_val, max_val, count):
    """Генерирует массив случайных чисел заданного размера в заданном диапазоне."""
    return [random.randint(min_val, max_val) for _ in range(count)]


def generate_shuffled_list(size):
    """Создает список от 0 до size-1 и перемешивает его случайным образом."""
    array = list(range(size))
    random.shuffle(array)
    return array


def read_list_from_file(file_path, element_type):
    """Читает массив из файла, приводя элементы к указанному типу."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    with open(file_path, 'r') as file:
        if element_type == 'int':
            try:
                mas = list(map(int, file.read().split()))
                return mas
            except ValueError:
                return
        return file.read().split()


def write_list_to_file(array, file_path):
    """Записывает массив в указанный файл."""
    with open(file_path, 'w') as file:
        file.write(' '.join(map(str, array)))


def main():
    parser = create_parser()
    args = parser.parse_args()
    rev = args.reverse
    visualize = args.visualize

    array = []

    if args.write_list:
        try:
            array = generate_list_from_input(args.write_list, args.type)
        except ValueError:
            print('Неверный тип данных')
            return

    elif args.generate_random:
        min_val, max_val, count = args.generate_random
        array = generate_random_list(min_val, max_val, count)

    elif args.generate_shuffle:
        array = generate_shuffled_list(args.generate_shuffle)

    elif args.readfile:
        array = read_list_from_file(args.readfile, args.type)
        if array is None:
            print('В файле содержатся не только числа')
            return

    print(f'Неотсортированный массив: {array}')
    if visualize:
        if args.type == 'str':
            sub_array = array.copy()
            sorted_array = my_sort(array, reverse=rev)
            array_for_sort = visualize_string_sort(sub_array, sorted_array)
            my_sort(array_for_sort, reverse=rev, visualize=True)
        else:
            sorted_array = my_sort(array, reverse=rev, visualize=True)
    else:
        sorted_array = my_sort(array, reverse=rev)
    print(f'Отсортированный массив: {sorted_array}')

    if args.writefile:
        write_list_to_file(array, args.writefile)


def visualize_string_sort(arr, sorted_arr):
    dictionary = {}
    array_for_visualize = []
    index = 1
    for elem in sorted_arr:
        dictionary[elem] = index
        index += 1
    for elem in arr:
        array_for_visualize.append(dictionary[elem])
    return array_for_visualize


if __name__ == "__main__":
    main()
