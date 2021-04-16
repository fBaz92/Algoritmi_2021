def poldo(lista, massimo=0, conta=0):
  if len(lista) ==0:
    return conta
  if massimo > lista[0] or conta == 0:
    #se mangio il panino
    conta1 = poldo(lista [1:], lista [0], conta+1)

    #se NON mangio il panino
    conta2 = poldo(lista [1:], massimo, conta)
    
    return max(conta1, conta2)

  else: 
    #non posso mangiare il panino
    return poldo(lista [1:], massimo, conta)

b = []
f = open("input.txt", "r")
n = int((f.readline()))

for i in range (n):
  b.append(int(f.readline()))


f2 = open("output.txt", "w")
soluzione = poldo(b)
f2.write(str(soluzione))
f2.close()