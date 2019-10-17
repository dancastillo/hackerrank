#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    neg = 0
    pos = 0
    netural = 0
    length = len(arr)

    for i in range(length):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else:
            netural += 1

    print(pos / length)
    print(neg / length)
    print(netural / length)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
