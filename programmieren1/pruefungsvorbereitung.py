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
    for _ in range(k + 1):
        n, rest = divmod(n, 10)
    return rest


def set_kth_digit(n, k, d):
    """
    >>> set_kth_digit(468, 0, 1)
    461
    >>> set_kth_digit(468, 1, 1)
    418
    >>> set_kth_digit(468, 2, 1)
    168
    >>> set_kth_digit(468, 3, 1)
    1468
    """
    left, right = divmod(n, 10**k)
    return ((left // 10) * 10 + d) * 10**k + right


def sum_digits(y):
    """
    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # use return rather than print in your code!
    >>> a
    6
    """
    result = 0

    while True:
        if y <= 0:
            break

        y, rest = divmod(y, 10)
        result += rest

    return result


def oddSum(L):
    """
    >>> oddSum([1,2,3,4])
    4
    >>> oddSum([])
    0
    >>> oddSum([2,4,6])
    0
    >>> oddSum([1,3,5])
    9
    """
    if len(L) <= 0:
        return 0

    digit = L.pop()

    if digit % 2 != 0:
        return digit + oddSum(L)
    return 0 + oddSum(L)


class Person:
    def __init__(self, name: str) -> None:
        self.name = name
        print("init")

    def __add__(self, other):
        return [self, other]

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


if __name__ == "__main__":
    doctest.testmod()
    print(locals())
