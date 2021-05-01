# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 23:09:10 2021

@author: franc
"""

def pillole(intere, mezze=0):
    
    if intere == 0 or (intere == 1 and mezze == 0):
        return 1
    elif mezze == 0 and intere != 0:
        return pillole(intere-1,mezze+1)
    else:
        return pillole(intere-1,mezze+1) + pillole(intere,mezze-1)
    

def pillole_memo(intere, mezze=0, memo = {}):
    
    key = str(intere)+"-"+str(mezze)
    if key in memo:
        return memo[key]
    else:
        if intere == 0 or (intere == 1 and mezze == 0):
            return 1
        elif mezze == 0 and intere != 0:
            memo[key] = pillole_memo(intere-1,mezze+1, memo)
            return memo[key]
        else:
            memo[key] = pillole_memo(intere-1,mezze+1,memo) + pillole_memo(intere,mezze-1,memo)
            return memo[key]
    
