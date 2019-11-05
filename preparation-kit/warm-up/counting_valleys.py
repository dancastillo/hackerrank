#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sea_level = 0
    valley_count = 0
    in_valley = False

    for i in range(n):
        if s[i] == 'U':
            sea_level += 1

            if sea_level >= 0:
                in_valley = False
        elif s[i] == 'D':
            sea_level -= 1

            if sea_level < 0:
                if not in_valley:
                    valley_count += 1
                in_valley = True

    return valley_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

