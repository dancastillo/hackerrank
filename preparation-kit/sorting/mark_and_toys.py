#!/bin/python3

import os

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    num_of_toys = 0

    print(prices)
    for i in range(len(prices)):
        k = k - prices[i]

        if k <= 0:
            break
        num_of_toys += 1
        
    return num_of_toys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()

