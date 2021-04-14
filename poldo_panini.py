# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 22:15:42 2021

@author: franc
"""

appoggio = [] 

def poldo(lista, massimo = 0, contatore = 0):
        
    global appoggio
       
    if len(lista) == 1:
        if lista[0] < massimo:  
            appoggio.append(contatore + 1)
        else:
            appoggio.append(contatore)
    
    for i in range(len(lista)):
        if massimo == 0 or lista[i] < massimo:
            poldo(lista[i:], lista[i], contatore + 1)
    
    return (appoggio)
    
        
b = [5,3,6,7,5,3]


soluzione = max(poldo(b))
print(soluzione)            