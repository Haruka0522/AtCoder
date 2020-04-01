# -*- coding: utf-8 -*-
from itertools import permutations, combinations
from fractions import gcd
from collections import Counter
from collections import deque
from math import sqrt
import bisect
import sys
input = sys.stdin.readline
def lcm(x, y):
    return (x*y//gcd(x, y))
def small_letters():
    return [chr(i) for i in range(97, 97+26)]
def capital_letters():
    return [chr(i) for i in range(65, 65+26)]
def base_10_to_N(x,n):
    if (int(x/n)):
        return base_10_to_N(int(x/n),n)+str(x%n)
    return(str(x%n))
def continual_letters(list_x):
    """example"""
    """[2,2,2,2,4,4,5,5,5,8,8,8,8,8] => [(2, 1), (4, 1), (5, 1), (8, 5)]"""
    result = []
    cnt = 1
    for i in range(len(list_x)-1):
        if list_x[i] == list_x[i+1]:
            cnt += 1
        else:
            num = list_x[i]
            cnt = 1
            result.append((num,cnt))
    result.append((list_x[-1],cnt))
    return result


def main():
    """ここに書いてね"""

if __name__ == '__main__':
    main()
