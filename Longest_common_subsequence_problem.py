#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(str1, str2):
    arr = [[0 for x in range(len(s1))] for y in range(len(s2))]
    for i in range(len(str2)):
        for j in range(len(str1)):
            if i==0 or j==0:
                if str2[i]==str1[j]:
                    arr[i][j]=1
                else:
                    arr[i][j]=0
            else :
                if str2[i]==str1[j] :
                    arr[i][j] = arr[i-1][j-1]+1
                else :
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1])
                    
       # print(arr[i])
    return arr[-1][-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
