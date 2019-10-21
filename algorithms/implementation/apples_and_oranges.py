#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleReaches = 0
    orangeReaches = 0

    for i in range(len(apples)):
        appleLands = a + apples[i]
        if appleLands >= s and appleLands <= t:
            appleReaches += 1
    for i in range(len(oranges)):
        orangeLands = b + oranges[i]
        if  orangeLands <= t and orangeLands >= s:
            orangeReaches += 1

    print(appleReaches)
    print(orangeReaches)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
