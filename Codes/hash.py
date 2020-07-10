#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:16:37 2020
 Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. 
 Then compute and print the result of .
@author: devyanshitiwari
"""

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    tuple1=tuple(integer_list)
    var=str(hash(tuple1))
    print(var)
