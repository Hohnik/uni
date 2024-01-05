import operator  # we don't know yet what this line does...

def another_add(x, y):
    """
    The next few lines are so called 'doc tests'
    in python (https://realpython.com/python-doctest/).
    These look like the interactive shell in python
    and resemble test cases that demonstrate correct
    useage and correct results for the current function.

    >>> another_add(3, 4) # should be 3+4
    7
    >>> another_add(4, 3) # should be 4+3
    7
    """
    # we don't know the following conditional statement yet
    # but it might be easy to understand its semantics.
    if x <= y:
        result = operator.add(x, y)
    else:
        # hmm, is this an add function?
        result = x - y
    return result

def is_prime(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    return isPrime


def smallest_factor(n: int):
    if is_prime(n):
        return n

    for i in range(2, n):
        if n % i == 0:
            return smallest_factor(int(n / i))
