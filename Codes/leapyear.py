#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 17:52:40 2020

@author: devyanshitiwari
"""

def is_leap(year):
    leap = False
    
    # Write your logic here
    
    if(year%4==0 and year%100 !=0):
      leap=True
    elif(year%100==0 and year%400==0):
       leap=True   
    
    
    return leap

year = 2100
print (is_leap(year))