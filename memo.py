# -*- coding: utf-8 -*-
from itertools import permutations, combinations
from fractions import gcd
from collections import Counter
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
    """[2,2,2,2,4,4,5,5,5,8,8,8,8,8] => [4,2,3,5]"""
    i,j = 0,0
    result = []
    k = len(list_x) - 1
    while(True):
        A = list_x[i]
        while(True):
            print(j)
            if list_x[j] != A:
                break
            if j >= k:
                break
            j += 1
        result.append(j-i)
        if i >= k:
            break
        i = j
    result[-1] += 1
    return result


def main():
    """ここに書いてね"""

if __name__ == '__main__':
    main()
