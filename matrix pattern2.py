# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 22:22:41 2020

@author: ADMIN
"""

n=int(input())
mx=[]
for i in range(n):
    row=list(map(int,input().split()))
    mx.append(row)
    
def func1(mx,i):
    n=len(mx)
    for ind in range(i,n-i):
        print(mx[i][ind],end=" ")
    for ind in range(i+1,n-i):
        print(mx[ind][n-1-i],end=" ")
    for ind in range(n-2-i,i,-1):
        print(mx[n-1-i][ind],end=" ")
    for ind in range(n-i-1,i,-1):
        print(mx[ind][i],end=" ")

def func(mx):
    n=len(mx)
    for i in range(n):
        func1(mx,i)
        print()