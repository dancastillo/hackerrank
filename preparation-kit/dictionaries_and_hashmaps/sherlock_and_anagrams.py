#!/bin/python3
import os

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0
    substrings = dict(enumerate(get_substrings(s), start=0))

    for i in substrings:
        for j in range(i + 1, len(substrings)):
            if len(substrings[i]) == len(substrings[j]):
                org_array = [0]*26
                for letter in substrings[i]:
                    org_array[ord(letter)-ord('a')] += 1
                    
                check_array = [0]*26
                for letter in substrings[j]:
                    check_array[ord(letter)-ord('a')] += 1

                if org_array == check_array:
                    count += 1

    return count


def get_substrings(s):
    return [s[i: j] for i in range(len(s))
            for j in range(i + 1, len(s) + 1)]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

