# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def routing(m,n):
    """
    

    Parameters
    ----------
    m : int
        numero di righe.
    n : int
        numero di colonne.
    
    Returns
    numero di cammini possibili di una matrice m x n
    -------
    int

    """
    print("ho chiamato {m} righe e {n} colonne".format(m=m,n=n))
    if m == 1:
        return 1
    elif n == 1:
        return 1
    else:
        return routing(m-1,n) + routing(m,n-1)
    
def routing_dp(m,n, memo={}):
    """
    

    Parameters
    ----------
    m : int
        numero di righe.
    n : int
        numero di colonne.
    memo : dict, optional
        Dizionario. Le chiavi sono le tuple della matrice riga colonna
        e il valore associato è il valore della chiamata 
        routing per quel valore. 
        The default is {}.

    Returns
    numero di cammini possibili di una matrice m x n
    -------
    int

    """
    
    print("ho chiamato {m} righe e {n} colonne".format(m=m,n=n))
    if (m,n) in memo.keys():
        return memo[(m,n)]
    else:
        if m == 1:
            return 1
        elif n == 1:
            return 1
        else:
            memo[(m,n)] = routing_dp(m-1,n,memo) + routing_dp(m,n-1,memo)
            memo[(n,m)] = routing_dp(m-1,n,memo) + routing_dp(m,n-1,memo)
            return memo[(m,n)]
        
        