#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:01:50 2020
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
@author: devyanshitiwari
"""

 if __name__ == '__main__':
    s = raw_input()

print any(i.isalnum()  for i in s)
print any(i.isalpha() for i in s)
print any(i.isdigit() for i in s)
print any(i.islower() for i in s)
print any(i.isupper() for i in s)

# The any() function returns True if any item in an iterable are true, otherwise it returns False.