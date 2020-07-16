#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 09:35:55 2020
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
@author: devyanshitiwari
"""



# Complete the solve function below.
def solve(s):
    s=s.capitalize()
    for i in s[:].split():
        s=s.replace(i,i.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
