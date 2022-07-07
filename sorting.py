#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    
    value = arr[-1]
    for i in range( n-1, -1, -1) :
        
        if value == arr[i]:
            continue
        elif value < arr[i]:
            arr[i+1]= arr[i]
            if value < arr[0]:
                arr[0] = value
        elif value > arr[i]: 
            arr[i+1] = value
            print (*arr)
            return       
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n,arr)
