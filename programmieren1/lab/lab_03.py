from collections import Counter, defaultdict
from lab_01_pp_primes import is_prime
import doctest


def max_product(lst:list):
    """
    let lst be a list of integers. Return the maximum product that can be formed using non-consecutive elements of lst.
    >>> max_product([10,3,1,9,2]) # 10*9
    90
    >>> max_product([5,10,5,10,5]) # 5*5*5
    125
    >>> max_product([9,6,7,10,5,10]) # 9*10*10
    900
    >>> max_product([9,6,7,10,5,10]) # 9*10*10
    900
    >>> max_product([])
    1
    """
    k = []

    match len(lst):
        case 0:
            return 1
        case 1:
            return lst[0]
    for idx, elem in enumerate(lst):
        if idx == 0:
            k.append(elem)
        elif idx == 1:
            k.append(max(elem, k[0]))
        else:
            k.append(max(elem * k[idx-2], k[idx-1]))
    return k[-1]

def remove_odd_indices(lst, odd, weight):
    """
    lst is a list, odd is a boolean. Return a new list with elements from ls
    removed at certain indices: If odd is True, remove elements at odd indic
    otherwise remove even indexed elements. The remaining elements are
    multiplied by weight.
    >>> s = [1, 2, 3, 4]
    >>> t = remove_odd_indices(s, True, 1)
    >>> s
    [1, 2, 3, 4]
    >>> t
    [1, 3]
    >>> l = [5, 6, 7, 8]
    >>> m = remove_odd_indices(l, False, 4)
    >>> m
    [24, 32]
    """
    # YOUR CODE HERE
    if odd:
        return list(map(lambda x: x*weight, lst[::2]))
    return list(map(lambda x: x*weight, lst[1::2]))

def merge(lst1, lst2):
    """Merges two sorted lists, lst1 and lst2. The new list contains all
    elements in sorted order.
    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    return sorted(lst1 + lst2)

def alternatingSum(lst):
    """
    Return the alternating sum of the integer or float elements
    in the list lst. An alternating sum of a sequence is a sum
    where the sign alternates from positive to negative or
    vice versa.
    >>> alternatingSum([5, 3, 8, 4])
    6
    >>> alternatingSum([])
    0
    """
    # YOUR CODE HERE.
    result = 0
    for i, number in enumerate(lst):
        result += (-1)**i * number
    return result

def is_anagram(s1, s2):
    """
    Decide whether a string s1 and a string s2 are anagrams.
    Use only lists in your solution.
    >>> is_anagram("","")
    True
    >>> is_anagram("abCdabCd","abcdabcd")
    True
    >>> is_anagram("abcdaabcd","aabbcddcb")
    False
    """

    #NOTE Fill the counting dictionaries
    s1_dct = {}
    for s1_value in s1:
        s1_value = s1_value.lower()
        if s1_value in s1_dct:
            s1_dct[s1_value] += 1
            continue
        s1_dct[s1_value] = 1

    s2_dct = {}
    for s2_value in s2:
        s2_value = s2_value.lower()
        if s2_value in s2_dct:
            s2_dct[s2_value] += 1
            continue
        s2_dct[s2_value] = 1

    return s1_dct == s2_dct

    #return Counter(s1.lower()) == Counter(s2.lower())

def rotateStringLeft(s:str, n):
    """
    The function takes a string s and a possibly-negative integer n.
    If n is non-negative, the function returns the string s rotated
    n places to the left. If n is negative, the function returns
    the string s rotated |n| places to the right.
    >>> rotateStringLeft('abcd', 1)
    'bcda'
    >>> rotateStringLeft('abcd',-1)
    'dabc'
    """

    slist = list(s)
    if n >= 0:
        slist.reverse()

    for i in range(abs(n)):
        popped = slist.pop()
        slist.insert(0, popped)

    if n >= 0:
        slist.reverse()
    return "".join(slist)

def caesar_cipher(message, shift):
    """
    A Caesar Cipher is a simple cipher that works by shifting
    each letter in the given message by a certain number. For
    example, if we shift the message "We Attack At Dawn" by 1
    letter, it becomes "Xf Buubdl Bu Ebxo".

    ceasar_cipher(message, shift) shifts the given message by
    'shift' many letters. You are guaranteed that 'message' is a
    string, and that 'shift' is an integer between -25 and 25.
    Capital letters should stay capital and lowercase letters
    should stay lowercase, and non-letter characters should
    not be changed. "Z" wraps around to "A".
    >>> caesar_cipher("We Attack At Dawn", 1)
    'Xf Buubdl Bu Ebxo'
    >>> caesar_cipher("zodiac",-2)
    'xmbgya'
    """
    capitalLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lowercaseLetters = list(map(lambda x: x.lower(), capitalLetters))

    result = ""
    for letter in message:

        if letter in lowercaseLetters:
            shiftedIndex = (lowercaseLetters.index(letter)+shift) % len(lowercaseLetters)
            result += lowercaseLetters[shiftedIndex]
            continue

        if letter in capitalLetters:
            shiftedIndex = (capitalLetters.index(letter)+shift) % len(capitalLetters)
            result += capitalLetters[shiftedIndex]
            continue

        result += letter
    return result

def most_frequent(L):
    """
    Return the most frequent element in a list L, resolving
    ties arbitrarily. L only has elements of scalar types.
    >>> most_frequent([2,5,3,4,6,4,2,4,5])
    4
    >>> most_frequent([2,3,4,3,5,3,6,3,7])
    3
    >>> most_frequent([42])
    42
    >>> most_frequent([])

    """
    return Counter(L).most_common()[0][0] if L else None

def is_anagram_dict(s1, s2):
    """
    Decide whether a string s1 and a string s2 are anagrams.
    Use only dictionaries in your solution.
    >>> is_anagram_dict("","")
    True
    >>> is_anagram_dict("abCdabCd","abcdabcd")
    True
    >>> is_anagram_dict("abcdaabcd","aabbcddcb")
    False
    """
    s1, s2 = s1.lower(), s2.lower()
    dicts = []
    for i, dictionary in enumerate([s1, s2]):
        dicts.append(defaultdict(int))
        for letter in dictionary:
            dicts[i][letter] += 1
    return dicts[0] == dicts[1]

# def most_popular_names():
#     """
#     Using the information in the file 'popular_names.txt' (see files attached to this lab), build two dictionaries, one for male names, and one for female names, and return the two dictionaries.
#     Come up with two reasonable doctests!
#     >>> most_popular_names()["males"]["James"]
#     '4,625,363'
#     >>> most_popular_names()["males"]["Tyler"]
#     '597,268'
#     >>> most_popular_names()["females"]["Amy"]
#     '683,154'
#     >>> most_popular_names()["females"]["Marie"]
#     '337,979'
#     """

#     males, females = defaultdict(str), defaultdict(str)

#     with open("../files/popular_names.csv", "r") as file:
#         for line in file:
#             if "#" in line:
#                 continue
#             _, maleName, maleNameCount, femaleName, femaleNameCount = line.split()
#             males[maleName] = maleNameCount
#             females[femaleName] = femaleNameCount
    
#     return {"males":males, "females": females}

def word_count():
    """
    Find a text file containing the complete works of
    William Shapespeare attached to this lab (see moodle course website).
    * Find the 20 most common words.
    * How many unique words are used?
    * How many words are used at least 5 times?
    * Write the 200 most common words, and their counts,
    to a file 'top200.txt'
    """
    with open("../files/shakespeare.txt") as file:
        counter = Counter()
        for line in file:
            counter.update(list(map(str.lower,line.split())))

        #Task1
        most_common_20 = counter.most_common(20)

        #Task2
        unique_words_count = len(counter)

        #Task3
        five_uses_words_count = 0
        for i, word in enumerate(counter.most_common()):
            if word[1] == 4:
                five_uses_words_count = i
                break

        #Task4
        with open("../files/top200.txt", "w+") as file:
            for wordTuple in counter.most_common(200):
                word, frequency = wordTuple
                file.write(f"{word}, {frequency}\n")
                
    return most_common_20, unique_words_count, five_uses_words_count, "files/top200.txt"

def make_primes():
    """
    Using a single (possibly nested) list comprehension, compute the set of prime numbers from 0 to
    99 (inclusive). Your list comprehension should return a list of lists, where the i-th list is the list of prime numbers in [i*10, (i*10)+9]. The result should look something like: [[2, 3, 5, 7], [11, 13, 17, 19], ...]. Use the known function is_prime(x) that returns True if x is prime
    and False otherwise.
    >>> type(make_primes())
    <class 'list'>
    >>> len(make_primes())
    10
    >>> make_primes()[0]
    [2, 3, 5, 7]
    >>> make_primes()[1]
    [11, 13, 17, 19]
    >>> make_primes()[9]
    [97]
    >>> make_primes()
    [[2, 3, 5, 7], [11, 13, 17, 19], [23, 29], [31, 37], [41, 43, 47], [53, 59], [61, 67], [71, 73, 79], [83, 89], [97]]
    """
    return [[number for number in range(i*10, i*10+10) if is_prime(number)] for i in range(10)]

def counter(lst: list) -> dict:
    """ 
    Use a single dictionary comprehension that maps each element of a list of items to the number of times it appears in that list, but only if it appears more than 2 times.

    >>> counter(["A","A","A","B","B","C","C","C","C","D"])
    {'C': 4, 'A': 3, 'B': 2, 'D': 1}
    >>> counter([])
    {}
    """
    dct = defaultdict(int)
    for elem in lst:
        dct[elem] += 1
    
    sortedList = sorted(dct.items(), key=lambda elem: -elem[1])
    return {letter:count for letter, count in sortedList}

def counter_freq_over_2(lst: list) -> dict:
    """ 
    Use a single dictionary comprehension that maps each element of a list of items to the number of times it appears in that list, but only if it appears more than 2 times.

    >>> counter_freq_over_2(["A","A","A","B","B","C","C","C","C","D"])
    {'A': 3, 'C': 4}
    >>> counter_freq_over_2([])
    {}
    """
    dct = defaultdict(int)
    for elem in lst:
        dct[elem] += 1
    return {letter:count for letter, count in dct.items() if count > 2}

"""
Compute without a computer
1. ZeroDevisionError
2. True
3. ZeroDevisionError
4. ct1(list)
    a = ['n', 5, True, True, (3,5),'n']
    b = [True, "n"]
    c = {}
    d = pointer to c dict


    c["n"] = ['n', 5, True, True, (3,5),'n']
    c[5] = [True, "n"]
    c[True] = 5
    c[True] = 2
    c[(3,5)] = True

    return -> {
            "n": ['n', 5, True, True, (3,5),'n'],
            5: [True, "n"],
            True: 2,
            (3,5): True
        }

5. ct1(list)
    x = [42, 30, 100]
    y = @pointer x
    z = [42, 30, 100]
    x = [42, 30, 100, 12]
    y,x = [45, 30, 100, 12]
    x = [100, 12]
    print -> "x = [100, 12]
    x = [100, 112]
    z = [30, 100]
    return 112, 12, 100

    print -> "ct = (112, 12, 100)"
    print -> "L = [42, 30, 100]"


6. make2d(cols, rows)
    my_matrix = [[0, 0], 
                 [0, 0], 
                 [0, 0]]
    my_matrix = [[42, 0], 
                 [42, 0], 
                 [42, 0]]
    print -> [[42, 0], 
              [42, 0], 
              [42, 0]]
"""

doctest.testmod()