#Trasforma lista di stringhe in lista di interi
def string_to_int(str_list):
  for i in range(len(str_list)):
    str_list[i] = int(str_list[i])
  return str_list


#Calcola riga per riga la somma degli elementi di un triangolo
#Non è ottimizzato per un cazzo ma funziona
#100/100 punti su ALGO2020
def calcola_somma(somma, riga):
  print(somma, " -- ", riga)
  
  if riga == []:
    print("risultato: " , somma)
    return somma
  else:
    if len(riga) == 1:
      somma.append(riga[0])
    else:      
      somma2 = somma[:]

      somma[0] += riga[0]
      somma.append(somma2[len(somma) -1 ] + riga[len(riga) -1])
      

      if(len(riga) > 2):
        for i in range(1,len(riga)-1):
          somma[i] = max(somma2[i-1] + riga[i], somma2[i]+ riga[i])
      
    calcola_somma(somma, string_to_int(f.readline().split()))
    return somma


f = open("input.txt", "r")
n = int((f.readline()))

ris = calcola_somma([], string_to_int(f.readline().split()))
ris.sort(reverse = True)
f.close()

f2 = open("output.txt", "w")
f2.write(str(ris[0]))
f2.close()
