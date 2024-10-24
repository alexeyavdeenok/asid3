import argparse
import random


def main():
    # Создание парсера аргументов
    parser = argparse.ArgumentParser(description='Обработка массива с различными функциями.')

    # Аргумент для ввода элементов массива через пробел
    parser.add_argument('-wl', '--write_list', type=str,
                        help='Ввод элементов массива через пробел')

    # Аргумент для типа элементов массива
    parser.add_argument('-t', '--type', choices=['str', 'int'], default='int',
                        help='Тип элементов массива (по умолчанию: int)')

    # Аргумент для генерации случайных значений
    parser.add_argument('-gr', '--generate_random', nargs=3, type=int,
                        help='Генерация массива заполненного случайными значениями: '
                             'минимальное число, максимальное число, количество чисел')

    # Аргумент для случайной перестановки n элементов
    parser.add_argument('-gs', '--generate_shuffle', type=int,
                        help='Случайная перестановка n элементов')

    # Аргумент для визуализации алгоритма
    parser.add_argument('-v', '--visualize', action='store_true', default=False,
                        help='Визуализация алгоритма (по умолчанию: False)')

    # Аргумент для чтения файла
    parser.add_argument('-r', '--readfile', type=str,
                        help='Чтение файла, получает путь к файлу')

    # Аргумент для чтения и записи в файл
    parser.add_argument('-rw', '--readwrite', nargs=2, type=str,
                        help='Чтение и запись в файл: путь до файла для чтения и путь до файла для записи')

    # Аргумент для сортировки по убыванию
    parser.add_argument('-rev', '--reverse', action='store_true', default=False,
                        help='Сортировка по убыванию (по умолчанию: False)')

    # Парсинг аргументов
    args = parser.parse_args()

    # Обработка аргументов
    array = []

    # Обработка ввода из аргументов
    if args.writelist:
        if args.type == 'int':
            array = list(map(int, args.writelist.split()))
        else:
            array = args.writelist.split()

    if args.generaterandom:
        min_val, max_val, count = args.generaterandom
        array = [random.randint(min_val, max_val) for _ in range(count)]

    if args.generatehuffle:
        array = list(range(args.generatehuffle))
        random.shuffle(array)

    if args.readfile:
        with open(args.readfile, 'r') as file:
            if args.type == 'int':
                array = list(map(int, file.read().split()))
            else:
                array = file.read().split()

    if args.readwrite:
        read_path, write_path = args.readwrite
        with open(read_path, 'r') as read_file:
            if args.type == 'int':
                array = list(map(int, read_file.read().split()))
            else:
                array = read_file.read().split()

        with open(write_path, 'w') as write_file:
            write_file.write(' '.join(map(str, array)))

    if args.reverse:
        array.sort(reverse=True)
    else:
        array.sort()

    # Вывод результата
    print("Отсортированный массив:", array)
    if args.visualize:
        # Здесь должна быть ваша логика для визуализации
        print("Визуализация включена (добавьте реализацию визуализации)")


if __name__ == "__main__":
    main()
