# -*- coding: utf-8 -*-

__author__ = 'Taras Drapalyuk <taras@drapalyuk.com>'
__date__ = '02.04.2017'


class QuickSort(object):
    def __init__(self, pivot_func):
        self.pivot_func = pivot_func

    def sort(self, array):
        if len(array) <= 1:
            return 0, array

        pivot_index = self.pivot_func(array)
        pivot = array[pivot_index]

        if pivot_index != 0:
            # swap the pivot element with the first element
            array[pivot_index], array[0] = array[0], array[pivot_index]
            pivot_index = 0

        i = 0
        for j, x in enumerate(array):
            if x <= pivot:
                if array[i] > array[j]:
                    # swap
                    array[i], array[j] = array[j], array[i]

                i += 1

        array[pivot_index], array[i - 1] = array[i - 1], array[pivot_index]
        pivot_index = i - 1

        # TODO: don't use new lists
        left = array[:pivot_index]
        right = array[pivot_index + 1:]

        current_count = len(array) - 1
        left_count, left_sorted = self.sort(left)
        right_count, right_sorted = self.sort(right)

        total_sorted = left_sorted + [pivot] + right_sorted
        total_count = current_count + left_count + right_count
        return total_count, total_sorted
