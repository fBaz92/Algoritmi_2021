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



""""
STAMPA PIASTRELLATURE COLORATE

Per tutte le funzioni la chiamata è questa:
(n, colore1 = colore piastrella in alto, colore2 = colore piastrella in basso, riga1 = riga già colorata in alto, riga2 = riga già colorata in basso" )
"""

def colore_libero(c1,c2):
  if c1 != 1 and c2 != 1:
    return 1
  elif c1 != 2 and c2 != 2:
    return 2
  else:
    return 3


def stampa_h(n,c1 = 0,c2 = 0,r1 = "",r2= ""):
  x = colore_libero(c1,c2)
  stampa_g(n, c1, x, r1, r2 + " " + str(x))
  stampa_f(n, c1, x, r1, r2 + " " + str(x) + " " + str(x))


def stampa_j(n,c1 = 0,c2 = 0,r1 = "",r2= ""):
  x = colore_libero(c1,c2)

  if n == 0:
    r1 = r1 + " " + str(x)
    print (r1)
    print (r2)
    print()
  
  else:
    stampa_f(n, x, c2, r1 + " " + str(x), r2)
    stampa_g( n-1, x, c2, r1 + " " + str(x) + " " + str(x), r2)


def stampa_g(n,c1 = 0,c2 = 0,r1 = "",r2= ""):
  x = colore_libero(c1, c2)

  if n == 0:
    r2 = r2 + " " + str(x)
    print(r1)
    print(r2)
    print()
  
  else:
    stampa_f(n, c1,x, r1, r2 + " " + str(x))
    stampa_j(n-1, c1, x, r1, r2 + " " + str(x) + " " + str(x))

def stampa_f(n,c1 = 0,c2 = 0,r1 = "",r2= ""):
  if n == 0:
    print(r1)
    print(r2)
    print()
  
  elif n == 1:
    x = colore_libero(c1,0)
    stampa_g(n-1, x, c2, r1 + " " + str(x), r2)

    x = colore_libero(c1,c2)
    stampa_f(n-1, x , x, r1 + " " + str(x), r2 + " " + str(x))
  
  else:
    
    x = colore_libero(c1,0)
    stampa_g(n-1, x, c2, r1 + " " + str(x), r2)


    x = colore_libero(c1,c2)
    stampa_f(n-1, x , x, r1 + " " + str(x), r2 + " " + str(x))

    x = colore_libero(c1, 0)
    stampa_h(n-2, x, c2, r1 + " " + str(x) + " " + str(x), r2)

""" 
PER I/O su file come chiede Rizzi nell'esercizio

in_file = open("input.txt", "r")
n = in_file.readline()
in_file.close()

from contextlib import redirect_stdout

with open('output.txt', 'w') as f:
    with redirect_stdout(f):
        print(f_memo(int(n)))
        stampa_f(int(n))

"""