#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []

    dict = {'(':')','{':'}','[':']',')':'(','}':'{',']':'['}

    def push(stack, char):
        stack.append(char)

    def pop(stack):
        if (len(stack) > 0):
            return stack.pop(-1)
        
    def top(stack):
        if (len(stack) > 0):
            return (stack[-1])
        else:
            return (-1)

    for i in s:
        if top(stack) == -1:
            push(stack, i)
        else:
            if dict[top(stack)] != i:
                push(stack, i)
            else:
                pop(stack)
    if stack == []:
        return('YES')
    else:
        return('NO')



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

