# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 20:05:28 2021

@author: franc

NB: non trattato a lezione
"""

def sum_up(n,numbers):
    
    if n == 0:
        return True
    
    for number in numbers:
        reminder = n - number
        if reminder < 0:
            return False
        elif reminder == 0:
            return True
        else:
            return sum_up(reminder,numbers)
    return False




def sum_up_memo(n, numbers, memo = {0:True}):
    if n in memo.keys():
        return memo[n]
    
    for number in numbers:
        reminder = n - number
        if reminder < 0:
            return False
        elif reminder == 0:
            return True
        else:
            memo[n] = sum_up_memo(reminder,numbers,memo)
            return memo[n]
    return False

