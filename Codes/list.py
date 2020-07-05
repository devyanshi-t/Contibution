#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 15:47:59 2020

@author: devyanshitiwari
"""
#Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    N = int(raw_input())
    i=0
    l1=[]
    for i in range (N):
        
        entry = raw_input().split()
        rc = entry[0]
        if rc=='insert':
         l1.insert(int(entry[1]), int(entry[2]))
        elif rc=='print':
          print(l1)
        elif rc=='remove':
         l1.remove(int(entry[1]))
        elif rc=='append':
         l1.append(int(entry[1])) 
        elif rc=='sort':
         l1.sort()
        elif rc=='pop':
         l1.pop()
        elif rc=='reverse':
         l1.reverse()
        
