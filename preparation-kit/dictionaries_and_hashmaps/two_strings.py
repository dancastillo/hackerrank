#!/bin/python3

import os

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    py_dict = dict.fromkeys(s1);
    for i in range(len(s2)):
        if s2[i] in py_dict:
            return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

