"""Шаблон модуля my_sort"""
import random


def my_sort(array, reverse=False, key=lambda x: x, cmp=None):
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
    sort_list(array, key, cmp, 0, len(array) - 1)
    return array


def sort_list(array, key, cmp, first, last):
    if first >= last:
        return
    else:
        q = random.choice(array[first:last + 1])
        i = first
        j = last
        while i <= j:
            while cmp(array[i], q) < 0:
                i += 1
            while cmp(array[j], q) > 0:
                j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        sort_list(array, key, cmp, first, j)
        sort_list(array, key, cmp, i, last)
