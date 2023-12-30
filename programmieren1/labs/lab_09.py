import time
import random

def intersect(L1, L2):
    """
    Returns a list with all different elements of both lists.
    Each element is only found once in the new list.

    It has a runtime of O(n**2) + O(n**2) == O(2 * n**2) -> O(n**2)
    """
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)

    res = []
    for e in tmp:
        if not (e in res):
            res.append(e)

    return res

def test_intersect():
    L1 = [1, 2, 3, 4, 5, 6]
    L2 = [4, 4, 5, 5, 6, 6, 7, 8, 9,]
    assert intersect(L1, L2) == [4, 5, 6]


def g(n):
    """ assume n >= 0
    Returns n squared.
    """
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1

    return x

def g_1(n):
    return n**2

def test_g():
    n = 12
    assert g(n) == g_1(n)


def search(lst, element):
    for x in lst:
        if x == element:
            return True
    return False

def test_search():
    assert search([1, 2, 3, 4, 5], 3)
    assert not search([1, 2, 3, 4, 5], 8)


def binary_search(lst, element):
    if len(lst) == 1:
        return False

    middle = len(lst) // 2
    if lst[middle] == element:
        return True

    return binary_search(lst[:middle], element) | binary_search(lst[middle:], element)

def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 3)
    assert not binary_search([1, 2, 3, 4, 5], 8)


def bubble_sort(lst: list):
    swapped = True
    while swapped:
        swapped = False
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
    return lst

def test_bubble_sort():
    lst = [2, 4, 1, 3, 6, 7, 5]
    assert bubble_sort(lst) == [1, 2, 3, 4, 5, 6, 7]


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

def test_selection_sort():
    lst = [2, 4, 1, 3, 6, 7, 5]
    assert selection_sort(lst) == [1, 2, 3, 4, 5, 6, 7]


def insertion_sort(lst: list):  # O(n**2) https://media.geeksforgeeks.org/wp-content/uploads/insertionsort.png
    swap_index = 1

    while swap_index < len(lst):

        index = swap_index
        while index >= 1 and lst[index] < lst[index-1]:
            lst[index], lst[index-1] = lst[index-1], lst[index]
            index -= 1

        swap_index += 1
    return lst

def test_insertion_sort():
    lst = [2, 4, 1, 3, 6, 7, 5]
    assert insertion_sort(lst) == [1, 2, 3, 4, 5, 6, 7]


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


def test_quick_sort():
    lst = [2, 4, 1, 3, 6, 7, 5]
    assert quick_sort(lst) == [1, 2, 3, 4, 5, 6, 7]


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

def test_merge_sort():
    lst = [2, 4, 1, 3, 6, 7, 5]
    assert merge_sort(lst) == [1, 2, 3, 4, 5, 6, 7]


def time_sorts(algos, size):
    results = {"algorithm": [], "time": []}
    for f in algos:
        results["algorithm"].append(f.__name__)
        lst = [i for i in range(size)]
        random.shuffle(lst)
        start = time.time()
        f(lst)
        stop = time.time()
        results["time"].append(stop - start)
    return results

def time_printer_string(n):
    result = ""
    algorithms = [quick_sort]
    time_table = time_sorts(algorithms, n)
    for algo, runtime in zip(time_table["algorithm"], time_table["time"]):
        result += f"{algo}: \t{runtime:.5}\n"

    return result


runs = [100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
for n in runs:
    print(n, time_printer_string(n), sep="\n")
    print()
