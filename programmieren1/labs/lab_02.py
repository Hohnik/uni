
def a_plus_abs_b(a,b):
    """
    return a+abs(b), but without calling abs.
    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    #a = -a if a < 0 else a
    absolute_b = -b if b < 0 else b
    return a+absolute_b

def two_of_three(i, j, k):
    """
    Return m*m + n*n, where m and n are the two smallest members of the positive numbers i, j, and k.
    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    numbers = [i,j,k]
    for _ in range(len(numbers)):
        for i in range(2):
            if numbers[i+1] < numbers[i]:
                numbers[i+1], numbers[i] = numbers[i], numbers[i+1] 
     
    return numbers[0]**2 + numbers[1]**2
        
def largest_factor(n):
    """Return the largest factor of n (n > 1 !) that is smaller than n.
    A factor divides a number evenly.
    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    for i in range(n-1,0, -1):
        if n % i == 0:
            return i

def double_eights(n):
    """Return true if n has two eights in a row.
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
    for digit in str(n):
        if int(digit) != 8:
            counter = 0
        else:
            counter += 1
            if counter == 2:
                return True
    return False

def getKthDigit(n, k):
    """
    Return the kth digit of n (an integer), starting from 0,
    counting from the right.
    >>> getKthDigit(789, 0)
    9
    >>> getKthDigit(789, 1)
    8
    >>> getKthDigit(789, 2)
    7
    >>> getKthDigit(789, 3)
    0
    >>> getKthDigit(-789, 0)
    9
    """
    return int(list(reversed(str(n)))[k]) if k < len(str(n)) else 0

def setKthDigit(n, k, d):
    """
    n is an integer, k is a non-negative integer and d is non-negative
    single digit (0 <= d <= 9). Return the number n with the kth digit
    replaced with d.
    >>> setKthDigit(468, 0, 1)
    461
    >>> setKthDigit(468, 1, 1)
    418
    >>> setKthDigit(468, 2, 1)
    168
    >>> setKthDigit(468, 3, 1)
    1468
    """
    n_cut_to_kth_digit = n // 10 ** k
    kth_digit = n_cut_to_kth_digit % 10
    n_with_zero_at_kth_digit = n - kth_digit * 10**k
    new_n = n_with_zero_at_kth_digit + d * 10**k

    return new_n

def sum_digits(y):
    """Sum all the digits of y. y is always nonnegative. Floor division
    and modulo might be helpful.
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
    summe = 0
    for string_digit in str(y):
        summe += int(string_digit)
    return summe

"""
Compute without a computer
xk(10,10) -> 23
xk(10,6) -> 23
xk(4,6) -> 4
xk(0,0) -> 25

how_big(7) -> "big"
how_big(12) -> "huge"
how_big(1) -> "small"
how_big(-1) -> "nothing"

bake(0,29)
    print: 1
    print: 29
    return 29
bake(1, "mashed potatoes")
    print: "mashed potatoes"
    return: "mashed potatoes"

ab(10, 20)
    print: 10
    print: "foo"

ct2(5)
    print: 2
    print: 6
    print: 13
    return: 3

print(ct2(5) + 1)
    print: 4
"""
# %%
