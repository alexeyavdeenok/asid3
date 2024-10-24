import random
import matplotlib.pyplot as plt
import time


def visualize_sort(func):
    def wrapper(array, *args, **kwargs):
        fig, ax = plt.subplots()
        bars = ax.bar(range(len(array)), array, color='blue')
        plt.ion()  # Interactive mode on

        def update_bars(array, color_indices=None):
            for idx, bar in enumerate(bars):
                bar.set_height(array[idx])
                if color_indices and idx in color_indices:
                    bar.set_color('red')
                else:
                    bar.set_color('blue')
            plt.pause(0.001)  # Pause for animation effect
            fig.canvas.draw()

        def visualize_swap(i, j):
            update_bars(array, color_indices=[i, j])
            time.sleep(0.001)  # Delay to visualize swap clearly

        # Inject the visualization into the sorting function
        kwargs['visualize_swap'] = visualize_swap

        result = func(array, *args, **kwargs)

        update_bars(array)  # Final update
        plt.ioff()  # Turn off interactive mode
        plt.show()  # Keep the final plot displayed
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
            return (y > x) - (y < x)
    sort_list(array, key, cmp, 0, len(array) - 1, visualize_swap)
    return array


def sort_list(array, key, cmp, first, last, visualize_swap):
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
                # Визуализация обмена элементов
                visualize_swap(i, j)
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        sort_list(array, key, cmp, first, j, visualize_swap)
        sort_list(array, key, cmp, i, last, visualize_swap)


# Пример использования
if __name__ == "__main__":
    array = [_ for _ in range(200)]
    random.shuffle(array)
    print("Исходный массив:", array)
    sorted_array = my_sort(array, reverse=True)
    print("Отсортированный массив:", sorted_array)
