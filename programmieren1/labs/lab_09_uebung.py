import math
import random
import time


def insertion_sort(lst):
    for i in range(1, len(lst)):
        offset = 0
        while lst[i - offset] < lst[i - offset - 1] and offset != i:
            lst[i - offset], lst[i - offset - 1] = (
                lst[i - offset - 1],
                lst[i - offset],
            )
            offset += 1

    return lst


random_list = list(range(1000))

# -_______________ ____________ ________________________

summe = 0
for i in range(100):
    random.shuffle(random_list)
    start = time.time()
    insertion_sort(random_list)
    end = time.time()
    summe += end - start
print(summe)


def selection_sort(lst:list)-> list:
    
    
