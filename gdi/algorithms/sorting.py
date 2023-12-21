from collections import deque
import pytest
import random


"""
Attribute von Sortieralgoritmen

    Rekursiv
    Returned kopie der Liste
    Laufzeitkomplexität
    Speicherkomplexität



"""

def bubble_sort(lst:list): #* O(n**2)
    swapped = True
    while swapped: 
        swapped = False
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j] 
                

def selection_sort(lst:list): #* O(n**2)
    min_number = -float("inf")

def insertion_sort(lst:list): #* O(n**2)
    ...

def quick_sort(lst:list): #* O(n * log(n))
    ...

def merge_sort(lst:list): #* O(n * log(n))
    left = lst[:len(lst)//2]
    if len(left) == 1:
        return left[0]
    
    right = lst[len(lst)//2:]
    if len(right) == 1:
        return right[0]

    return left+right


@pytest.mark.parametrize("f",[bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort])
def test_sorts(f):
    lst = [i for i in range(10)]
    random.shuffle(lst)
    assert f(lst) == [i for i in range(10)]
