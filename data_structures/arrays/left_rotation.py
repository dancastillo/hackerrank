#!/bin/python3

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    arr = []
    temp = []

    for i in range(len(a)):
        if i < d:
            temp.append(a[i])
        else:
            arr.append(a[i])

    arr = arr + temp

    for i in range(len(arr)):
        print(arr[i], end=" ")
