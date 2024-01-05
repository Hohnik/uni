import pytest
import random


"""
Attribute von Sortieralgoritmen
    Rekursiv
    Returned kopie der Liste
    Laufzeitkomplexität
    Speicherkomplexität
"""

def bubble_sort(lst: list):
    swapped = True
    while swapped:
        swapped = False
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
    return lst


def selection_sort(lst: list):  # O(n**2)
    swap_index = 0

    while swap_index < len(lst):
        min_value = float("inf")
        min_value_index = 0

        for i in range(swap_index, len(lst)):
            if lst[i] < min_value:
                min_value_index = i
                min_value = lst[i]

        lst[swap_index], lst[min_value_index] = lst[min_value_index], lst[swap_index]
        swap_index += 1

    return lst


def insertion_sort(lst: list):  # O(n**2) https://media.geeksforgeeks.org/wp-content/uploads/insertionsort.png
    swap_index = 1

    while swap_index < len(lst):

        index = swap_index
        while index >= 1 and lst[index] < lst[index-1]:
            lst[index], lst[index-1] = lst[index-1], lst[index]
            index -= 1

        swap_index += 1
    return lst


def quick_sort(lst: list):  # O(n * log(n)) https://www.baeldung.com/wp-content/uploads/sites/4/2021/06/Quicksort-891x1024-1.png
    if len(lst) == 1:
        return lst
    if len(lst) == 0:
        return []

    left = []
    right = []
    pivot = lst[-1]

    for i in range(len(lst)-1):
        if lst[i] < pivot:
            left.append(lst[i])
        else:
            right.append(lst[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(lst: list):  # O(n * log(n)) https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Merge_sort_algorithm_diagram.svg/300px-Merge_sort_algorithm_diagram.svg.png
    if len(lst) <= 1:
        return lst

    middle = len(lst)//2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)

def merge(left, right):
    sortedList = []

    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            sortedList.append(left[0])
            left.pop(0)
        else:
            sortedList.append(right[0])
            right.pop(0)

    while len(left) != 0:
        sortedList.append(left[0])
        left.pop(0)

    while len(right) != 0:
        sortedList.append(right[0])
        right.pop(0)

    return sortedList


funcs = [bubble_sort, selection_sort, insertion_sort, quick_sort, merge_sort]
@pytest.mark.parametrize("f", [funcs[i % len(funcs)] for i in range(5)])
def test_sorts(f):
    lst = [i for i in range(1000)]
    random.shuffle(lst)
    assert f(lst) == [i for i in range(1000)]
