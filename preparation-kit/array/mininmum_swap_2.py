#!/bin/python3

import os

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap = 0

    dic = {el:i for i, el in enumerate(arr)}
    for i in range(len(arr), 0, -1):
        if i != arr[i-1]:
            idx = dic[i]        
            dic[i] = i - 1
            dic[arr[i-1]] = idx
            arr[i-1], arr[idx] = arr[idx], arr[i-1]
            swap += 1

    return swap


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

