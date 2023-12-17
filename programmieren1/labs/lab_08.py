def count_occurrences(t, n, x):
    """
    Return the number of times that x is equal to one of the
    first n elements of iterator t.
    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s2, 3, 10)
    2
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(s, 1, 3) # Only iterate over 3
    1
    >>> count_occurrences(s, 3, 2) # Only iterate over 2, 2, 2
    3
    >>> list(s) # Ensure that the iterator has advanced the right amount
    [1, 2, 1, 4, 4, 5, 5, 5]
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 6, 6, 2, 2, 2, 5])
    >>> count_occurrences(s2, 6, 6)
    2
    """
    counter = 0
    step_counters = 0
    while step_counters != n:
        if x == next(t):
            counter += 1
        step_counters += 1
    return counter

def repeated(t, k):
    """
    Return the first value in iterator t that appears k times in a row,
    calling next on t as few times as possible.
    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1

    counter = 0
    last = None

    while t:
        elem = next(t)

        counter = counter +1 if elem == last else 1
        
        if counter == k:
            return elem
        
        last = elem

def matches(a, b):
    """Return the number of values k such that A[k] == B[k].
    >>> matches([1, 2, 3, 4, 5], [3, 2, 3, 0, 5])
    3
    >>> matches("abdomens","indolence")
    4
    >>> matches("abcd","dcba")
    0
    >>> matches("abcde","edcba")
    1
    >>> matches("abcdefg","edcba")
    1
    """
    counter = 0
    for x,y in zip(a,b):
        if x == y:
            counter += 1
    return counter
    
def palindrome(s):
    """Return whether s is the same sequence backward and forward.
    >>> palindrome([3, 1, 4, 1, 5])
    False
    >>> palindrome([3, 1, 4, 1, 3])
    True
    >>> palindrome('seveneves')
    True
    >>> palindrome('seven eves')
    False
    """
    is_same = True
    for x,y in zip(s, s[::-1]):
        if x != y:
            is_same = False
    return is_same

def generate_constant(x):
    """
    A generator function that repeats the same value x forever.
    >>> two = generate_constant(2)
    >>> next(two)
    2
    >>> next(two)
    2
    >>> sum([next(two) for _ in range(100)])
    200
    """
    while True:
        yield x

def black_hole(seq, trap):
    """A generator that yields items in seq until one of them matches trap, in
    which case that value should be repeatedly yielded forever.
    >>> trapped = black_hole([1, 2, 3], 2)
    >>> [next(trapped) for _ in range(6)]
    [1, 2, 2, 2, 2, 2]
    >>> list(black_hole(range(5), 7))
    [0, 1, 2, 3, 4]
    """
    # Your code here
    for elem in seq:
        if elem == trap:
            while True:
                yield trap
        yield elem

def filter_iter(iterable, f):
    """
    Generates elements of iterable for which f returns True.
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even))
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    # Your code here.
    iterable = iter(iterable)
    while True:
        try:
            elem = next(iterable)
            if f(elem):
                yield elem
        except:
            return None

def differences(it):
    """
    Yields the differences between successive terms of iterable it.
    >>> d = differences(iter([5, 2, -100, 103]))
    >>> [next(d) for _ in range(3)]
    [-3, -102, 203]
    >>> list(differences([1]))
    []
    """
    # Your code here.

    it = iter(it)

    elem = None
    elem2 = next(it)

    while True:
        try:
            elem = elem2
            elem2 = next(iter(it))
            yield elem2-elem
        except:
            return



#* Compute without a computer
def compute():
    """
    >>> def infinite_generator(n):
    ...    yield n
    ...    while True:
    ...        n += 1
    ...        yield n
    >>> gen_obj = infinite_generator(1)
    >>> next(gen_obj)
    1
    >>> next(gen_obj)
    2
    >>> def rev_str(s):
    ...     for i in range(len(s)):
    ...         yield from s[i::-1]
    >>> hey = rev_str("hey")
    >>> next(hey)
    'h'
    >>> next(hey)
    'e'
    >>> next(hey)
    'h'
    >>> list(hey)
    ['y', 'e', 'h']
    >>> def add_prefix(s, pre):
    ...     if not pre:
    ...         return
    ...     yield pre[0] + s
    ...     yield from add_prefix(s, pre[1:])
    >>> school = add_prefix("schooler", ["pre", "middle", "high"])
    >>> next(school)
    'preschooler'
    >>> list(map(lambda x: x[:-2], school))
    ['middleschool', 'highschool']
    """

"""
>>> next(infinite_generator)
TypeError
>>> list(gen_obj)
MemoryError
"""
