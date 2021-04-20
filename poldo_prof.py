# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:15:27 2021

@author: franc
"""

panino = [3,10,9,7,5,8,4]


"""

"""
def num_max_panini(lista,t=0,last_panino_index=None, score=0):
    """
    
    Parameters
    ----------
    t : int
        indice a cui sono attualmente.
    last_panino_index : int
        indice dell'ultimo panino.

    Returns
    -------
    num_max_panini : int.
        numero massimo di panini che posso mangiare 
        nella sequenza poldo

    """
    #guardo se ho mangiato o meno un panino e scelgo se non mangiare un panino
    if last_panino_index == None:
        if t >= len(lista):
        #ho scorso tutta la lista e non posso più magiare panini
            return score
        #prendo il caso maggiore tra mangiare il panino o non mangiare il panino
        return max(num_max_panini(lista, t+1,t, score+1), num_max_panini(lista, t+1, None, 0))
    
    #altrimenti significa che ho mangiato il panino
    else:
        if t >= len(lista):
        #ho scorso tutta la lista e non posso più magiare panini
            return score
        
        if lista[t] >= lista[last_panino_index]:
            #se trovo un panino più pesante non posso mangiarlo
            #e quindi proseguo richiamando un problema più piccolo
            return num_max_panini(lista, t+1, last_panino_index, score)
        
        return max(num_max_panini(lista, t+1, last_panino_index, score), num_max_panini(lista, t+1, t, score+1))
    
    
def num_max_panini_memo(lista,t=0,last_panino_index=None, score=0, memo = {}, history = []):

    
    if history in memo.keys():
        return memo[history]
        
    else:
        
        #guardo se ho mangiato o meno un panino e scelgo se non mangiare un panino
        if last_panino_index == None:
            if t >= len(lista):
                return 0
            #prendo il caso maggiore tra mangiare il panino o non mangiare il panino
             
            tmp = max(num_max_panini_memo(lista, t+1, None, 0, memo, history), num_max_panini_memo(lista, t+1,t, score+1, memo, [i for i in history].append(t)))
            memo[history] = tmp
            return memo[history] 
            
            
        #altrimenti significa che ho mangiato il panino
        else:
            
            if t >= len(lista):
                #ho scorso tutta la lista e non posso più magiare panini
                memo[history] = score
                return score
            
            if lista[t] >= lista[last_panino_index]:
                #se trovo un panino più pesante non posso mangiarlo
                #e quindi proseguo richiamando un problema più piccolo
                 
                tmp = num_max_panini_memo(lista, t+1, last_panino_index, score, memo)
                memo[history] = tmp
                return tmp
                
        
            tmp = max(num_max_panini_memo(lista, t+1, last_panino_index, score, memo, history), num_max_panini_memo(lista, t+1, t, score+1, memo, [i for i in history].append(t)))
            memo[history] = tmp
            return tmp
   
   
   
   
   

    
   
a = num_max_panini_memo(lista=panino)
            
            

