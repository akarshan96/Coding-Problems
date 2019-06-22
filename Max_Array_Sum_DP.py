#!/bin/python3
# https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    result = [0] * len(arr)
    for i,val in enumerate(arr):
        if i == 0:
            result[i] = max(0,val)
        elif i == 1:
            result[i] = max(arr[i - 1],val)
        else:
            result[i] = max(val + result[i-2], result[i-1], val)
    return result[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
