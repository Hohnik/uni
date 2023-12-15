import math
import random
import timeit

def bubble_sort(L:list) -> list:
    return 1

def shell_sort(L:list) -> list:
    return 1+1



lst = [math.floor(random.random()*10) for _ in range(1000)]
timeit.timeit("bubble_sort(lst)", number=1)
timeit.timeit("shell_sort(lst)", number=1)