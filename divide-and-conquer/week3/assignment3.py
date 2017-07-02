# -*- coding: utf-8 -*-
from quicksort import QuickSort

__author__ = 'Taras Drapalyuk <taras@drapalyuk.com>'
__date__ = '20.03.2017'


def first(array):
    """Returns index of first element"""
    return 0


def last(array):
    """Returns index of last element"""
    return len(array) - 1


def median(array):
    """Returns index of median value

    >>> median([8, 2, 4, 5, 7, 1])
    2
    >>> median([4, 5, 6, 7])
    1
    >>> median([4, 6, 7])
    1

    :return: index 
    """
    first_index = 0
    middle_index = (len(array) - 1) / 2
    last_index = len(array) - 1

    return sorted([
        (array[first_index], first_index),
        (array[middle_index], middle_index),
        (array[last_index], last_index),

    ], key=lambda (x, i): x)[1][1]


def get_comparisons(pivot_func):
    with open('QuickSort.txt') as f:
        array = [int(l) for l in f.readlines()]

    qsort = QuickSort(pivot_func=pivot_func)
    comparisons, sorted_array = qsort.sort(array)

    # Validate sort result
    assert all(sorted_array[i] == el for i, el in enumerate(sorted(array)))

    return comparisons


if __name__ == '__main__':
    # 1 first element as pivot
    first_count = get_comparisons(pivot_func=first)
    print('First:\t%s' % first_count)

    # 2 last element as pivot
    last_count = get_comparisons(pivot_func=last)
    print('Last:\t%s' % last_count)

    # 3 median element as pivot
    median_count = get_comparisons(pivot_func=median)
    print('Median:\t%s' % median_count)
