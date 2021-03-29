# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:49:33 2021

@author: franc
"""
def f(n):
    assert n >= 0
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return f(n-1) + g(n-1) + h(n-2)
    
def g(n):
    assert n >= 0
    if n == 0:
        return 1
    else:
        return f(n) + g(n-1)

def h(n):
    assert n >= 0
    return f(n) + g(n)


