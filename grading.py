#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    for i in range(0,len(grades)):
        if grades[i] < 38:
            continue
        else:
            for j in range(grades[i]+1,101):
                if j % 5 == 0 and j-grades[i] < 3:
                    grades[i] = j               
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
