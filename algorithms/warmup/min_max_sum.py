#!/bin/python3


def miniMaxSum(arr):
    arr.sort()
    max_sum = 0
    min_sum = 0

    for i in range(len(arr)):
        if i == 0:
            min_sum += arr[i]
        elif i == len(arr) - 1:
            max_sum += arr[i]
        else:
            min_sum += arr[i]
            max_sum += arr[i]

    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
