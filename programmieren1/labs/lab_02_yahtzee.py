import random as rnd
from timeit import timeit
import seaborn as sns
import pandas as pd
import numpy as np


def main():
    PlayThreeDiceYahtzee(buildDice())

def handToDice(hand:tuple) -> tuple:
    """
    The function takes a hand, which is a 3-digit integer, and returns 3 values, each of the 3 dice in the hand.
    >>> handToDice(123)
    (1, 2, 3)
    >>> handToDice(214)
    (2, 1, 4)
    """
    return tuple(int(number) for number in str(hand))
    
def diceToOrderedHand(a:int,b:int,c:int) -> int:
    """
    this func takes 3 dice and returns them in a hand, which is a 3-digit integer. However, even if the dice are unordered, the resulting hand must be ordered so that the largest die is on the left and the smallest die is on the right.
    >>> diceToOrderedHand(1,2,3)
    321
    >>> diceToOrderedHand(6,5,4)
    654
    >>> diceToOrderedHand(1,4,2)
    421
    """
    hand = (a,b,c)
    result = 0

    for i, number in enumerate(sorted(hand)):
        result += number*10**i

    return result

def playStep2(hand:tuple, dice:int) -> tuple:
    """
    Given the current hand and future dice read from the LSB, calculate the best play and 
    return a tuple of the hand after one play and the remaining dice.
    >>> playStep2(413, 2345)
    (544, 23)
    >>> playStep2(544, 23)
    (443, 2)
    >>> playStep2(544, 456)
    (644, 45)
    >>> playStep2(555, 2345)
    (555, 2345)
    """
    a, b, c = handToDice(hand)
    if isPairOfThree(hand):
        return (diceToOrderedHand(a,b,c), dice)

    if isPairOfTwo(hand):
        if a == b:
            c = dice % 10
        else:
            a = dice % 10
        dice //= 10
        return (diceToOrderedHand(a,b,c), dice)
    
    b = dice % 10
    dice //= 10
    c = dice % 10
    dice //= 10
    return (diceToOrderedHand(a,b,c), dice)

def score(hand:tuple) -> int:
    """
    >>> score(432)
    4
    >>> score(532)
    5
    >>> score(443)
    18
    >>> score(633)
    16
    """
    if isPairOfThree(hand):
        return int(20 + (hand/111)*3)

    if isPairOfTwo(hand):
        return int(10 + int(str(hand)[1])*2)
    if isNoPair(hand):
        return int(hand // 100)

def PlayThreeDiceYahtzee(dice:int) -> tuple:
    """
    >>> PlayThreeDiceYahtzee(2312413)
    (432, 4)
    >>> PlayThreeDiceYahtzee(2315413)
    (532, 5)
    >>> PlayThreeDiceYahtzee(2345413)
    (443, 18)
    """
    first_dice_roll = playStep1(dice)
    second_dice_roll = playStep2(*first_dice_roll)
    hand, _ = playStep2(*second_dice_roll)
    game_score = score(hand) 
    return (hand, game_score)
 
def playStep1(dice:int) -> tuple:
    """
    >>> playStep1(123456)
    (654, 123)
    >>> playStep1(987654)
    (654, 987)
    >>> playStep1(333555)
    (555, 333)
    """
    a = dice % 10
    dice //= 10
    b = dice % 10
    dice //= 10
    c = dice % 10
    dice //= 10
    return (diceToOrderedHand(a,b,c), dice)

def isPairOfThree(hand:int) -> bool:
    """
    >>> isPairOfThree(555)
    True
    >>> isPairOfThree(321)
    False
    """
    if hand in [x*111 for x in range(10)]:
        return True
    return False
    
def isPairOfTwo(hand: int) -> bool:
    """
    >>> isPairOfTwo(441)
    True
    >>> isPairOfTwo(644)
    True
    >>> isPairOfTwo(321)
    False
    """
    hand_str = str(hand)
    if hand_str[0] == hand_str[1] or hand_str[1] == hand_str[2]:
        return True
    return False

def isNoPair(hand: int) -> bool:
    """
    >>> isNoPair(444)
    False
    >>> isNoPair(442)
    False
    >>> isNoPair(321)
    True
    """
    if not isPairOfThree(hand) and not isPairOfTwo(hand):
        return True
    return False

def buildDice():
    rnd_str = [str(rnd.randint(1,6)) for _ in range(7)]
    return int("".join(rnd_str))

if __name__ == "__main__":
    dataSet = [ (i, timeit(stmt=main, number=i)) for i in range(1,21)]
        


    frame = pd.DataFrame(dataSet, columns=["Iterations","Time"])
    print(frame)
    sns.set_theme()
    sns.relplot(data=frame, x="Iterations", y="Time")