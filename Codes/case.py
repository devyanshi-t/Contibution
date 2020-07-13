#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 10:25:35 2020

@author: devyanshitiwari

You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.
"""
def swap_case(s):
    x=""
    for i in s:
        if i.islower():
            x=x+i.upper()
        else:
         x=x+i.lower()
    return x

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print (result)
