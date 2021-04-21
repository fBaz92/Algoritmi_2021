""" sol vecchia
def poldo(lista, massimo=0, conta=0):
  if len(lista) ==0:
    return conta
  if massimo > lista[0] or conta == 0:
    conta1 = poldo(lista [1:], lista [0], conta+1)
    conta2 = poldo(lista [1:], massimo, conta)
    
    return max(conta1, conta2)
  else: return poldo(lista [1:], massimo, conta)
"""

""""
def poldo(lista, massimo=0, conta=0):
  if len(lista) ==0:
    return conta
  if massimo > lista[0] or conta == 0:
    conta1 = poldo(lista_minori(lista[1:], lista[0]), lista [0], conta+1)
    conta2 = poldo(lista [1:], massimo, conta)
    
    return max(conta1, conta2)
  else: return poldo(lista [1:], massimo, conta)


def lista_minori(lista, elemento):
  lista2 = []

  for e in lista:
    if(e < elemento):
      lista2.append(e)

  return lista2
"""





"""
SOLUZIONE CON MEMOIZZAZIONE (?)
35 punti su ALGO2020

#La chiave così fa schifo, ma almeno tengo traccia sia di t che di last_index
"""

panini = []
memo = {}

def poldo_memo(t=0, last_index=-1):
  global memo
  global panini 

  
  if t >= len(panini):
    #se indice t >= lunghezza vett panini non posso più mangiare nulla
    return 0
  else:
    if (str(t)+"-"+str(last_index) not in memo):

      if ( panini[t] >= panini[last_index]) and last_index != -1:
        #Se non posso mangiare il panino e se ne ho già mangiato qualcuno
        memo[str(t)+"-"+str(last_index)] = poldo_memo(t+1, last_index)
      else:
        #Calcolo max tra mangiare e non mangiare il panino
        memo[str(t)+"-"+str(last_index)] = max( poldo_memo(t+1, last_index), 1+ poldo_memo(t+1, t))

  print (str(t) , "-"  , last_index , ": " , memo[str(t)+"-"+str(last_index)])
  return memo[str(t)+"-"+str(last_index)]


f = open("input.txt", "r")
n = int((f.readline()))

for i in range (n):
  panini.append(int(f.readline()))


f2 = open("output.txt", "w")
soluzione = poldo_memo()
f2.write(str(soluzione))
f2.close()