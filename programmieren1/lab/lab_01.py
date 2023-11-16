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


print_result = print(another_add(another_add(3, 4), another_add(4, 5)))
print(print_result)
