# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def piastrellature(n):
    """
    

    Parameters
    ----------
    n : int
        lunghezza del bagno.

    Returns
    -------
        Questa funzione ricorsiva ritorna
        il numero di piastrellature possibili
        di un bagno 1xn con piastrelle 1x1 e 
        1x2.
        Soluzione puramente ricorsiva

    """
    #check di sicurezza su cosa do dentro alla funzione
    assert type(n) == int
    assert n>0
    
    if n == 1:
        return 1
    elif n == 2: 
        return 2
    else:
        return piastrellature(n-1) + piastrellature(n-2)
    
    
def piastrellature_memo(n, memo = {0:1,1:1,2:2}):
    """
    

    Parameters
    ----------
    n : int
        lunghezza del bagno.
        
    memo: dict
        dizionario con i valori dei sottoproblemi. Ho inserito 
        di default i casi base

    Returns
    -------
        Questa funzione ricorsiva ritorna
        il numero di piastrellature possibili
        di un bagno 1xn con piastrelle 1x1 e 
        1x2.
        Soluzione con memoization

    """
    
    assert type(n) == int
    assert n>0
    
    if n in memo.keys():
        return memo[n]
    else:
        """
        if n == 1:
            return 1
        elif n == 2: 
            return 2
        else:"""
        memo[n] = piastrellature_memo(n-1, memo) + piastrellature_memo(n-2, memo)
        return memo[n]
        
    