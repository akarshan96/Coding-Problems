#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    stack = []
    max_area = 0
    elem = 0
    area = -1

    def push(stack, char):
        stack.append(char)

    def pop(stack):
        if (len(stack) > 0):
            return stack.pop(-1)
            
    def top(stack):
        if (len(stack) > 0):
            return (stack[-1])
        else:
            return (None)

    for i, val in enumerate(h):
        
        if len(stack) == 0:
            push(stack, i)
        else:
            if(top(stack) != None):
                if (val > h[top(stack)]):
                    push(stack, i)
                else:
                    while(True):
                        if(len(stack) > 0):
                            if(val < h[top(stack)]):
                                elem = pop(stack)
                                if(len(stack) > 0):
                                    area = h[elem] * (i - top(stack) - 1)
                                    print(area)
                                else:
                                    area = h[elem] * i
                                    print(area)
                                if area > max_area:
                                    max_area = area

                            else:
                                push(stack,i)
                                break
                        else:
                            push(stack,i)
                            break
    return(max_area)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()

