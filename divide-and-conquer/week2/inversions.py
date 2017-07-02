# -*- coding: utf-8 -*-

__author__ = 'Taras Drapalyuk <taras@drapalyuk.com>'
__date__ = '20.03.2017'


def merge_and_count_split_inv(a, b):
    array = []
    count = 0
    i, j, = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            array.append(a[i])
            i += 1

        elif a[i] > b[j]:
            array.append(b[j])
            count += len(a[i:])
            j += 1

    array.extend(a[i:])
    array.extend(b[j:])

    return array, count


def count_inversions(array):
    n = len(array)
    if n == 1:
        return array, 0

    a, b = array[:n / 2], array[n / 2:]

    a, count_a = count_inversions(a)

    b, count_b = count_inversions(b)

    array, count_split = merge_and_count_split_inv(a, b)

    total_count = count_a + count_b + count_split
    return array, total_count


if __name__ == '__main__':
    array = [1, 3, 5, 2, 4, 6]
    array = [1, 2, 3, 5, 4]
    array_sorted, count = count_inversions(array)
    print(array)
    print(array_sorted)
    print(count)
