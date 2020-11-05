# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:57:15 2020

@author: ADMIN
"""
import turtle


def func():
    f=1
    n=70
    tur=turtle.Turtle()
    tur.penup()
    tur.setpos(0,0)
    tur.color("black")
    j=0
    while(j<n):
        if(f==1):
            i=0
            while(i<=n-1):
                tur.dot()
                turtle.goto(i,j)
                i=i+10
        if(f==0):
            i=n-1
            while(i>-1):
                tur.dot()
                turtle.goto(i,j)
                i=i-10
        f=(f+1)
        if(f==2):
            f=0
        j=j+10
    turtle.done()
    
func()