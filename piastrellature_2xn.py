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



"""
implementazione con memoizzazione
"""



memo_f = {}
memo_g = {}

def f_memo(n):
    
    global memo_f 
    global memo_g
    
    assert n>=0
    if n in memo_f.keys():
        return memo_f[n]
    else:
        if n == 0:
            memo_f[n] = 1
        elif n == 1:
            memo_f[n] = 2
        else:
            memo_f[n] = f_memo(n-1) + g_memo(n-1) + h_memo(n-2)
        
        return memo_f[n]

def g_memo(n):
    
    global memo_g
    global memo_f
    
    if n in memo_g.keys():
        return memo_g[n]
    else:
        assert n >= 0
        
        if n == 0:
            memo_g[n] = 1
        else:
            memo_g[n] =  f_memo(n) + g_memo(n-1)
        
        return memo_g[n]

def h_memo(n):
    assert n >= 0
    return f_memo(n) + g_memo(n)
