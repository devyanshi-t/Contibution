#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:57:17 2020

@author: devyanshitiwari
"""

import math
import os
import random
import re
import sys


n = int(input().strip())

if n%2==1:
    print("Weird")
elif n%2==0 and  n>=2 and n<=5:
    print ("Not Weird")
elif n%2==0 and  n>=6 and n<=20:
    print("Weird")
elif  n%2==0 and n>20:
    print("Not Weird")