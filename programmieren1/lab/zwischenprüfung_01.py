import doctest

def a2(x, y):
    """
    >>> a2(10,4)
    6
    >>> a2(10,-4)
    6
    """
    if y < 0:
        y = -y
    return x - y

def counter(L):
    """
    >>> counter([1, 1, 1])
    {1: 3}
    >>> counter([1, 2, 1])
    {1: 2, 2: 1}
    >>> counter([1, 2, 3])
    {1: 1, 2: 1, 3: 1}
    """
    dct = {}
    for num in L:
        if num in dct:
            dct[num] += 1
            continue
        dct[num] = 1
    return dct

def odd_mul(L1, L2):
    """
    >>> odd_mul([], [])
    0
    >>> odd_mul([], [1])
    0
    >>> odd_mul([2], [2])
    0
    >>> odd_mul([1, 2, 3, 4], [1, 2, 3, 4])
    20
    """
    if len(L1) != len(L2):
        return 0

    result = 0
    for x, y in zip(L1[1::2], L2[1::2]):
        result += x * y
    return result

doctest.testmod()