# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 22:11:03 2020

@author: ADMIN
"""

import turtle

def func():
    tur=turtle.Turtle()
    tur.setpos(0,0)
    n=70
    second=int(n/2)
    turtle.goto(second-1,second-1)
    turtle.goto(second-1,second)
    turtle.goto(second,second-1)
    turtle.goto(second,second)
    turtle.done()
    
    
func()