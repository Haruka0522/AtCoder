# -*- coding: utf-8 -*-
from itertools import permutations, combinations
from fractions import gcd
from collections import Counter
from math import sqrt
import sys
input = sys.stdin.readline
def lcm(x, y):
    return (x*y//gcd(x, y))
def small_letters():
    return [chr(i) for i in range(97, 97+26)]
def capital_letters():
    return [chr(i) for i in range(65, 65+26)]


def main():
    """ここに書いてね"""
    N = int(input())
    A_list = [int(input()) for i in range(N)]
    ans = 0
    counter = Counter(A_list)
    for i in counter.values():
        if i % 2 == 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()

