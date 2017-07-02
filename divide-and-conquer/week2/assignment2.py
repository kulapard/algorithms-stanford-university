# -*- coding: utf-8 -*-
from inversions import count_inversions

__author__ = 'Taras Drapalyuk <taras@drapalyuk.com>'
__date__ = '20.03.2017'

if __name__ == '__main__':
    with open('IntegerArray.txt') as f:
        array = [int(l) for l in f.readlines()]

    _, inversions = count_inversions(array)
    print(inversions)
