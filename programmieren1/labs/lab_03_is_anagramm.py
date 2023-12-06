from collections import Counter, defaultdict

def is_anagram_my_solution(s1, s2):
    """
    Decide whether a string s1 and a string s2 are anagrams.
    Use only dictionaries in your solution.
    >>> is_anagram_my_solution("","")
    True
    >>> is_anagram_my_solution("abCdabCd","abcdabcd")
    True
    >>> is_anagram_my_solution("abcdaabcd","aabbcddcb")
    False
    """
    return Counter(s1.lower()) == Counter(s2.lower())

def is_anagram_dict1(s1, s2):
    """
    Decide whether a string s1 and a string s2 are anagrams.
    Use only dictionaries in your solution.
    >>> is_anagram_dict1("","")
    True
    >>> is_anagram_dict1("abCdabCd","abcdabcd")
    True
    >>> is_anagram_dict1("abcdaabcd","aabbcddcb")
    False
    """
    s1, s2 = s1.lower(), s2.lower()
    dicts = []
    for i, dictionary in enumerate([s1, s2]):
        dicts.append(defaultdict(int))
        for letter in dictionary:
            dicts[i][letter] += 1
    return dicts[0] == dicts[1]

def is_anagram_dict2(s1, s2:list):
    """
    Decide whether a string s1 and a string s2 are anagrams.
    Use only lists in your solution.
    >>> is_anagram_dict2("","")
    True
    >>> is_anagram_dict2("abCdabCd","abcdabcd")
    True
    >>> is_anagram_dict2("abcdaabcd","aabbcddcb")
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

    #NOTE Check if they have the same structure the same
    return s1_dct == s2_dct