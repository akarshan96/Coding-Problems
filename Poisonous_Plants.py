#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    stack = []
    li_of_stack = []
    new_list = []
    count = 1

    pointer = 0


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


    for i in range(len(p) - 1, -1, -1):
        if i != 0:
            if p[i] > p[i - 1]:
                push(stack, p[i])
                li_of_stack.insert(0, stack)
                stack = []
            else:
                push(stack, p[i])
        else:
            push(stack, p[i])
            li_of_stack.insert(0, stack)
    print (li_of_stack)

    while len(li_of_stack) != 1:

        if i != 0:
            if i >= len(li_of_stack) :
                count += 1
                i = 0
                continue

            pop(li_of_stack[i])
            if not li_of_stack[i]:
                li_of_stack.remove(li_of_stack[i])
                continue

            if li_of_stack[i - 1][0] > top(li_of_stack[i]):
                temp = li_of_stack[i] + li_of_stack[i - 1]
                li_of_stack.remove(li_of_stack[i])
                li_of_stack.remove(li_of_stack[i - 1])
                i -= 1
                li_of_stack.insert(i,temp)
        i += 1
    if count > 0
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
