import doctest
import math


def a_plus_abs_b(a, b):
    """
    >>> a_plus_abs_b(2,3)
    5
    >>> a_plus_abs_b(2,-3)
    5
    >>> a_plus_abs_b(-1,4)
    3
    >>> a_plus_abs_b(-1,-4)
    3
    """
    return int(a + math.sqrt(b**2))


def two_of_three(i, j, k):
    """
    >>> two_of_three(1, 2,3)
    5
    >>> two_of_three(5,3,1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    numbers = [i, j, k]

    for idx in range(len(numbers) - 1):
        if numbers[idx] > numbers[idx + 1]:
            numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]

    return numbers[0] ** 2 + numbers[1] ** 2


def largest_factor(n):
    """
    >>> largest_factor(15)
    5
    >>> largest_factor(80)
    40
    >>> largest_factor(13)
    1
    """
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return i

    return 1


def double_eights(n):
    """
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    counter = 0
    while True:
        if counter == 2:
            return True
        if n <= 0:
            return False

        n, last = divmod(n, 10)
        if last == 8:
            counter += 1
        else:
            counter = 0


def get_kth_digit(n, k):
    """
    >>> get_kth_digit(789, 0)
    9
    >>> get_kth_digit(789, 1)
    8
    >>> get_kth_digit(789, 2)
    7
    >>> get_kth_digit(789, 3)
    0
    >>> get_kth_digit(-789, 0)
    9
    """
    n = abs(n)
    rest = None
    for i in range(k + 1):
        n, rest = divmod(n, 10)
    return rest


if __name__ == "__main__":
    doctest.testmod()
