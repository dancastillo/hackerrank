#!/bin/python3
import os

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    tallest = -1
    tallestCount = 0

    for i in range(len(ar)):
        if ar[i] > tallest:
            tallest = ar[i]
            tallestCount = 1
        elif ar[i] == tallest:
            tallestCount += 1

    return tallestCount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
