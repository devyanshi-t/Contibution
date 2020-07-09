#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 18:45:32 2020
You are given the firstname and lastname of a person on two different lines.
 Your task is to read them and print the following:
@author: devyanshitiwari
"""

def print_full_name(a, b):
    x=' ';
    print ("Hello "+a+x+b+"! "+"You just delved into python.")

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)