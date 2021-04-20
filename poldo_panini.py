# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 22:15:42 2021

@author: franc



#old solution
appoggio = [] 

def poldo(lista, massimo = None, contatore = 0):
        
    global appoggio
       
    if len(lista) == 1:
        if lista[0] < massimo:  
            appoggio.append(contatore + 1)
        else:
            appoggio.append(contatore)
    
    for i in range(len(lista)):
        if massimo is None or lista[i] < massimo:
            if massimo is None:
                poldo(lista[i:], lista[i], contatore + 1)
            else:
                massimo = lista[i]
                tmp = [j for j in lista[i:] if j < massimo]  
                poldo(tmp, massimo, contatore + 1)
    
    return (appoggio)
    
"""
    

e = [8,0,9,8,5,1,8,4,7]
b = [5,3,6,7,5,3]

def trova_successivi(lista):
    """
    

    Parameters
    ----------
    lista : list
        lista dei pesi dei panini.

    Returns
    -------
    tuple
        restituisce una tupla che contiene una lista di liste dei prossimi 
        panini che posso mangiare e i rispettivi massimi.
        
    """
    return [([element for element in lista[index:] if element < lista[index]], lista[index]) for index in range(len(lista))]


def get_score(lista, massimo, score = 0):
    if len(lista) == 0:
        return score
    else:
        if lista[0] < massimo:
            return get_score(lista[1:], lista[0], score + 1)
        else:
            return get_score(lista[1:], massimo, score)



appoggio = []

def poldo2(lista, massimo = 0, contatore = 0):
    
    global appoggio
    for index in range(len(lista)-1):
        appoggio.append(get_score(lista[index+1:],lista[index],1))
    
    tmp = max(appoggio)
    
    appoggio = []
    
    return tmp
        


appoggio2 = []    
def poldo3(lista, massimo = 0, contatore = 0):
    
    global appoggio2
    if len(lista) == 0:
        return contatore
    else:
        tmp = trova_successivi(lista)
        for coppia in tmp:
            appoggio2.append(poldo3(coppia[0], coppia[1], contatore + 1))

poldo3(e)






