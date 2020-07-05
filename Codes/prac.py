#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:40:06 2020

@author: devyanshitiwari
"""

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

    arr.sort()
    g=max(arr)
    rg=0
    for i in arr:
        if rg<i and rg<g:
          rg=i
    print (rg)