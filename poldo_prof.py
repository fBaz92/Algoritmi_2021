# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:15:27 2021

@author: franc
"""

panino = [3,10,9,8,5,8,4]


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
    
    
def num_max_panini_memo(lista,t=0,last_panino_index="inf", score=0, memo = {}, history = []):

    
    if tuple(history) in memo.keys():
        if tuple(history) == (): 
            return 0
        else:
            return memo[tuple(history)]
    
   #else
        
        
        
        
        
        
        
        """
        #guardo se ho mangiato o meno un panino e scelgo se non mangiare un panino
        if last_panino_index == "inf":
            if t >= len(lista):
                return 0
            #prendo il caso maggiore tra mangiare il panino o non mangiare il panino
            
            history_2 = history.copy()
            history_2.append(t)
            tmp = max(num_max_panini_memo(lista, t+1, "inf", 0, memo, history), num_max_panini_memo(lista, t+1,t, score+1, memo, history_2))
            memo[tuple(history)] = tmp
            history_2 = []
            return tmp 
            
            
        #altrimenti significa che ho mangiato il panino
        else:
            
            if t >= len(lista):
                #ho scorso tutta la lista e non posso più magiare panini
                if tuple(history) == ():
                    memo[("inf")] = score
                    return score
                else:
                    memo[tuple(history)] = score
                    return score
            
            if lista[t] >= lista[last_panino_index]:
                #se trovo un panino più pesante non posso mangiarlo
                #e quindi proseguo richiamando un problema più piccolo
                 
                tmp = num_max_panini_memo(lista, t+1, last_panino_index, score, memo)
                memo[tuple(history)] = tmp
                return tmp
             
            history_2 = history.copy()
            history_2.append(t)        
            tmp = max(num_max_panini_memo(lista, t+1, last_panino_index, score, memo, history), num_max_panini_memo(lista, t+1, t, score+1, memo, history_2))
            memo[tuple(history)] = tmp
            history_2 = []
            return tmp
   """
   
   
   
   

    
   
a = num_max_panini_memo(lista=panino)
            
            

