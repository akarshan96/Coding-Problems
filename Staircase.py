#!/bin/python3

import math
import os
import random
import re
import sys

memo = []
# Complete the stepPerms function below.
def stepPerms(n):
    if memo:
        if memo[n] != -1:
            return memo[n]
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 4

    else:
        result = stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n - 3)
        memo[n] = result
        return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())
        if n > 4:
            memo = (n + 1) * [-1]
            memo[1] = 1
            memo[2] = 2
            memo[3] = 4

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
