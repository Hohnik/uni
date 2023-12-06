import doctest
def main():
    doctest.testmod()

def oddCount(lst) -> int:
    """ 
    return the number of odd integers in lst
    
    >>> oddCount([0,1,2,3,4,5])
    3
    >>> oddCount([])
    0
    >>> oddCount([0,2,4,6,8])
    0
    >>> oddCount([3,5,7,9,111])
    5
    """
    if len(lst) == 0: #NOTE Basecase I know for sure
        return 0

    counter = 1 if lst[0] % 2 != 0 else 0 #NOTE Todo in this iteration
    return counter + oddCount(lst[1:])  #NOTE return and connection to the next iteration

def oddSum(lst) -> int:
    """ 
    return the sum of all odd integers in lst
    
    >>> oddSum([0,1,2,3,4,5])
    9
    >>> oddSum([])
    0
    >>> oddSum([0,2,4,6,8])
    0
    >>> oddSum([3,5,7,9,111])
    135
    """
    if len(lst) == 0:
        return 0

    value = lst[0] if lst[0] % 2 != 0 else 0
    return value + oddSum(lst[1:])

def oddsOnly(lst) -> int:
    """ 
    return a list with all odd integers in lst
    
    >>> oddsOnly([0,1,2,3,4,5])
    [1, 3, 5]
    >>> oddsOnly([])
    []
    >>> oddsOnly([0,2,4,6,8])
    []
    >>> oddsOnly([3,5,7,9,111])
    [3, 5, 7, 9, 111]
    """
    if len(lst) == 0:
        return []

    value = [lst[0]] if lst[0] % 2 != 0 else []
    return value + oddsOnly(lst[1:])

def maxOdd(lst) -> int:
    """ 
    return the biggest odd number in the lst. If there is no oddNumber return None.
    
    >>> maxOdd([0,1,2,3,4,5])
    5
    >>> maxOdd([])
    0
    >>> maxOdd([0,2,4,6,8])
    0
    >>> maxOdd([3,5,7,9,111])
    111
    """
    if not lst:
        return 0

    return max(lst[0], maxOdd(lst[1:])) if lst[0] % 2 != 0 else maxOdd(lst[1:])

def hasConsecutiveDigits_parameter_version(n: int, last_digit = None):
    """ 
    >>> hasConsecutiveDigits_parameter_version(12345)
    False
    >>> hasConsecutiveDigits_parameter_version(11234)
    True
    >>> hasConsecutiveDigits_parameter_version(112334)
    True
    >>> hasConsecutiveDigits_parameter_version(-112334)
    True
    >>> hasConsecutiveDigits_parameter_version(-12345)
    False
    >>> hasConsecutiveDigits_parameter_version(0)
    False
     """

    if n == 0:
        return False

    n = n//10 if n >= 0  else n//10 +1 #NOTE Nessesary because floor devision rounds numbers like 4.75 down to 4, but it also rounds -4.25 DOWN to the next smaller integer -5
    return last_digit == n%10 or hasConsecutiveDigits_parameter_version(n, n%10)

def hasConsecutiveDigits(n: int):
    """ 
    >>> hasConsecutiveDigits(12345)
    False
    >>> hasConsecutiveDigits(11234)
    True
    >>> hasConsecutiveDigits(112334)
    True
    >>> hasConsecutiveDigits(-112334)
    True
    >>> hasConsecutiveDigits(-12345)
    False
    >>> hasConsecutiveDigits(0)
    False
     """
    if n == 0:
        return False
    
    current_digit = n%10
    n = n//10 if n >= 0  else n//10 +1 #NOTE Nessesary because floor devision rounds numbers like 4.75 down to 4, but it also rounds -4.25 DOWN to the next smaller integer -5
    next_digit = n%10
    return current_digit == next_digit or hasConsecutiveDigits(n)

def alternatingSum_parameter_version(lst:list, counter = 0):
    """
    >>> alternatingSum_parameter_version([1,2,3,4,5])
    3
    >>> alternatingSum_parameter_version([10,20,30,40])
    -20
    >>> alternatingSum_parameter_version([])
    0
    """
    if lst == []:
        return 0
    
    return lst[0] * (-1)**counter + alternatingSum_parameter_version(lst[1:], counter+1)

def alternatingSum(lst:list):
    """
    >>> alternatingSum([1,2,3,4,5])
    3
    >>> alternatingSum([10,20,30,40])
    -20
    >>> alternatingSum([])
    0
    """
    if len(lst) == 1:
        return lst[0]
    
    if lst == []:
        return 0
    
    return lst[0] - lst[1] + alternatingSum(lst[2:])

def is_palindrome_recursion(strng, index = 0):
    """
    Test if a string of len >= 1 is a palindrom. 
    >>> is_palindrome_recursion("anna")
    True
    >>> is_palindrome_recursion("Anna")
    True
    >>> is_palindrome_recursion("Herbert") 
    False
    >>> is_palindrome_recursion("A") 
    True
    """
    strng = strng.lower()
    
    if len(strng) <= 1:
        return True
    
    return strng[0] == strng[-1] and is_palindrome_recursion(strng[1:-2])

def is_palindrome_recursion_parameter_version(strng, index = 0):
    """
    Test if a string of len >= 1 is a palindrom. 
    >>> is_palindrome_recursion_parameter_version("anna")
    True
    >>> is_palindrome_recursion_parameter_version("Anna")
    True
    >>> is_palindrome_recursion_parameter_version("Herbert") 
    False
    >>> is_palindrome_recursion_parameter_version("A") 
    True
    """
    strng = strng.lower()
    
    
    if index+1 == len(strng):
        return strng[index] == strng[-1-index]
    
    
    return strng[index] == strng[-1-index] and is_palindrome_recursion_parameter_version(strng, index +1)

def is_palindrome_loop(strng):
    """
    Test if a string of len >= 1 is a palindrom.
    >>> is_palindrome_loop("anna")
    True
    >>> is_palindrome_loop("Anna")
    True
    >>> is_palindrome_loop("Herbert") 
    False
    >>> is_palindrome_loop("A") 
    True
    """
    strng = strng.lower()

    for elem_front, elem_back in zip(strng, strng[::-1]):
        if elem_front != elem_back:
            return False
        
    return True

def num_eights(pos):
    """
    Takes a positive integer and return the number of 8ths found
    >>> num_eights(12348)
    1
    >>> num_eights(12345)
    0
    >>> num_eights(88888) 
    5

    """
    if pos == 0:
        return 0

    return 1 + num_eights(pos//10) if pos % 10 == 8 else num_eights(pos // 10)

def merge(dict1:dict, dict2:dict):
    """
    Takes a positive integer and return the number of 8ths found
    >>> merge({'a': 1, 'b': 2, 'c': 3}, {})
    {'a': 1, 'b': 2, 'c': 3}
    >>> merge({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2, 'c': 3})
    {'a': 2, 'b': 4, 'c': 6}
    >>> merge({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'd': 4, 'e': 5})
    {'a': 2, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    >>> merge({},{})
    {}
    """
    for key, value in dict2.items():
        if dict1.get(key):
            dict1[key] += value
            continue
        dict1[key] = value
    return dict1

""" Python Questions

1. What is the definition of a type in Python? List at least four examples of types built into Python
int, str, dict, list, tuple
A type is the way to tell python how to handle different data structures in memory and have different prebuilt functions for them

2. What is an expression? What is a statement? Give an example of each.
An expression is a code snipet, that returns something / evaluates to something:
sorted([2,1,3,4]) -> returns a list
A statement is code that is processed by the interpreter and maybe saved in memory but has no return.

3. What is the difference between a mutable and an immutable type? Give an example of each.
Mutable types are changeable without having to make a copy of the data structure. Lists are a muteable type, you can edit list items any time.
Imutable types cant be changed after creation. Strings are an example of this. They cant be changed but you can make a copy of it and process it that way.

4. What is a parameter ? What is an argument? How are they related?
A parameter is, what you declare at the definition of a function.
A argument is, what you pass into a function while calling it. 
While declaring the functions signature, you define what arguments someone can pass into the function via your parameters

5. What is the difference between a function definition and a function call ? Give an example of each.
A functions definition wont run any code inside the function. It creates the function in memory to be called later.
def myfunc():
    print("Hello World")
A function call will run the pre defined code and returns something.
myfunc()
"""



if __name__ == "__main__":
    main()
