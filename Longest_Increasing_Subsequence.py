#!/bin/python3
#   https://www.hackerrank.com/challenges/longest-increasing-subsequent/problem
import math
import os
import random
import re
import sys

# Complete the longestIncreasingSubsequence function below.
def longestIncreasingSubsequence(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(n):
        if i == 0:
            continue
        else:
            for j in range(i):
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i],dp[j] + 1)
    return(max(dp))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = longestIncreasingSubsequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
