# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 09:30:26 2021

@author: franc
"""

def routing_ostacoli(griglia, memo={}):
    """
    

    Parameters
    ----------
    griglia : list of lists
        lista che contiene gli ostacoli e i permessi
        *: permesso
        x: ostacolo
    memo : dictionary
        Dizionario che contiene i 
        valori delle chiamate ricorsive per 
        implementare la programmazione dinamica. The default is {}.

    Returns
    -------
    int
        numero di possibili routing data la griglia.

    """
    
    n = len(griglia)
    m = len(griglia[0])
    
    if n == 1:
        if 'x' in griglia[0]:
            return 0
        else:
            return 1
    elif m == 1:
        if 'x' in [i[0] for i in griglia]:
            return 0
        else:
            return 1
    else:
        if griglia[0][1] == 'x':
            #se a destra ho una x devo eliminare tutta la riga e quindi chiamo 
            #solo il caso con una riga in meno 
            griglia.pop(0)
            return routing_ostacoli(griglia)
        elif griglia[1][0] == 'x':
            #devo costruire una nuova griglia dove cancello tutti i 
            #primi elementi della prima riga
            #di fatto cancello la colonna
            griglia = [i[1:] for i in griglia]
            return routing_ostacoli(griglia)
        else:
            griglia1 = [i[1:] for i in griglia]
            griglia.pop(0)
            return routing_ostacoli(griglia1) + routing_ostacoli(griglia)
        

def routing_ostacoli_dp(griglia, memo={}):
    """
    

    Parameters
    ----------
    griglia : list of lists
        lista che contiene gli ostacoli e i permessi
        *: permesso
        x: ostacolo
    memo : dictionary
        Dizionario che contiene i 
        valori delle chiamate ricorsive per 
        implementare la programmazione dinamica. The default is {}.

    Returns
    -------
    int
        numero di possibili routing data la griglia.

    """
    
    n = len(griglia)
    m = len(griglia[0])
    
    if n == 1:
        if 'x' in griglia[0]:
            return 0
        else:
            return 1
    elif m == 1:
        if 'x' in [i[0] for i in griglia]:
            return 0
        else:
            return 1
    
    #dynamic programming
    elif griglia in memo.keys():
        return memo[griglia]
    
    
    else:
        if griglia[0][1] == 'x':
            #se a destra ho una x devo eliminare tutta la riga e quindi chiamo 
            #solo il caso con una riga in meno 
            chiave = griglia
            chiave.pop(0)
            memo[griglia] = routing_ostacoli(chiave)
            result = memo[griglia]
            griglia.pop(0)
            return result
        
        elif griglia[1][0] == 'x':
            #devo costruire una nuova griglia dove cancello tutti i 
            #primi elementi della prima riga
            #di fatto cancello la colonna
            
            chiave = [i[1:] for i in griglia]
            memo[griglia] = routing_ostacoli(chiave)
            result = memo[griglia]
            griglia = [i[1:] for i in griglia]
            return routing_ostacoli(griglia)
        else:
            chiave1 = [i[1:] for i in griglia]
            chiave2 = griglia
            chiave2.pop(0)
            result = routing_ostacoli(chiave1) + routing_ostacoli(chiave2)
            memo[griglia] = result
            return result
        

    
griglia1 = ['*','x','*','*','x','*']
griglia2 = ['*','*','*','*','*','*']
griglia = [griglia1,griglia2,griglia2,griglia2,griglia1,griglia2]

print(routing_ostacoli(griglia))


griglia1 = ['*','x','*','*','*','x','*','*','*','x','*','*','*','x','*','*']
griglia2 = ['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*']
griglia3 = ['*','*','x','*','*','*','*','*','*','*','*','*','*','*','*','*']
griglia = [griglia1,griglia2,griglia3,griglia1,griglia1,griglia1,griglia1,griglia1,griglia1,griglia1,griglia1,griglia1,griglia1,griglia1]
print(routing_ostacoli(griglia))