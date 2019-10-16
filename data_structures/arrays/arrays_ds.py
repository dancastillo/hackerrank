#!/bin/python3
import os


def reverse_array(a):
    return a[::-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverse_array(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
    