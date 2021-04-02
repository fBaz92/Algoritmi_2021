def hanoi(n_dischi, inizio, appoggio, fine):
#Sposta una torre di n dischi da un piolo inizio ad uno fine

  if(n_dischi == 1):
    #Sposto ultimo elemento di "inizio" in "fine"
    fine.append(inizio[(len(inizio) - 1)])
    inizio.pop(len(inizio) -1 )
    

  else:
    #Sposto torre di n-1 dischi da inizio ad appoggio
    hanoi(n_dischi -1, inizio, fine, appoggio)

    #Sposto base da inizio a fine
    fine.append(inizio[(len(inizio) - 1)])
    inizio.pop(len(inizio) -1 )

    #Sposto torre di n-1 dischi da appoggio a fine
    hanoi(n_dischi-1, appoggio, inizio, fine)

def print_lists(A,B,C):
  print("A: " , A)
  print("B: " , B)
  print("C: " , C)


n = int(input('Inserire numero di dischi: '))
A = []
B = []
C = []


for i in range(n):
  A.append(n-i)

print_lists(A,B,C)

print("Eseguo algoritmo...")
hanoi(n, A, B,C)

print_lists(A,B,C)



"""
soluzione francesco bazzani
"""

#creo la lista di caratteri
def create_list_char(n):
    return [chr(ch) for ch in range(ord('a'), ord('a')+n)]


# Recursive Python function to solve the tower of hanoi
  
def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
          
# Driver code
n = 4
TowerOfHanoi(n,'A','B','C') 
# A, C, B are the name of rods
  
# Contributed By Dilip Jain

