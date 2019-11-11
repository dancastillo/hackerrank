#!/bin/python3
import os

# Complete the repeatedString function below.
def repeatedString(s, n):
    a_count = s.count('a')
    a_return = 0

    loops = n // len(s)
    a_return = a_count * loops
    
    remaining_str = n % len(s)
    a_return += s[0: remaining_str].count('a')

    return a_return


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

