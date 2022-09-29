#!/bin/python3

import math
import os
import random
import re
import sys


def countSwaps(a):
    swap_number = 0
    for i in range(len(a)):
        for j in range(0,len(a)-1):
            if (a[j] > a[j + 1]): 
                (a[j], a[j + 1]) = (a[j+1],a[j])
                swap_number += 1 
                
    print("Array is sorted in", swap_number, "swaps.")     
    print("First Element:",a[0])
    print("Last Element:",a[-1])
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
1
