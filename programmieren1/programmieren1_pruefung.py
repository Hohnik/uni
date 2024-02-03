def filter_zsum(n: int, fltr: list):
    """
    >>> filter_zsum(12345, [2,4,6,8])
    9
    """

    n_str = str(n)
    n_lst = list(n_str)
    n_filtered = filter(lambda elem: elem not in fltr, n_lst)
    return sum(map(int, n_filtered))


def minGerade(L):
    pass


class Chapter:
    pass


def stuck(seq: int, trap: int):
    pass


def is_sauberzahl(n):
    pass


def string_matches(L):
    pass
