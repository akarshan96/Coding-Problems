#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(arr):
    # complete this function
    dict = {}
    i_dict = {}
    stack = []
    return_arr = []

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

    def left_scan(i,val):
        while(i > 0):
            i -= 1
            if arr[i] >= val:
                stack.append(i)
            else:
                break;
            
    def right_scan(i,val):
        while(i < len(arr)):
            if arr[i] >= val:
                push(stack,i)
            else:
                break
            i += 1

    for i,val in enumerate(arr):
        left_scan(i,val)
        stack = stack [::-1]
        right_scan(i,val)
        print(arr[i],val,stack)
        if len(stack) == 1:
            if val not in dict:
                dict[val] = 1
        else:
            if val not in dict:
                dict[val] = stack[-1] - stack[0] + 1
            else:
                dict[val] = max(stack[-1] - stack[0] + 1,dict[val])
        stack = []
        
    print(dict)
    for i in dict:
        if dict[i] not in i_dict:
            i_dict[dict[i]] = i
        else:
            i_dict[dict[i]] = max(i,i_dict[dict[i]])
    print(i_dict)

    prev_value = 0
    return_arr = [0] * len(arr)
    for i in range(len(arr), 0, -1):
        if prev_value == 0:
            prev_value = i_dict[i]
            return_arr[i - 1] = i_dict[i]
        else:    
            if i in i_dict:
                if i_dict[i] < prev_value:
                    return_arr[i - 1] = prev_value
                else:
                    return_arr[i - 1] = i_dict[i]
                    prev_value = return_arr[i - 1]
            else:
                return_arr[i - 1] = prev_value  
                
    return(return_arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
