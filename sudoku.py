# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:07:23 2021

@author: franc
"""

import numpy as np 

board = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,0],[0,0,0,0,8,0,0,7,0]]




def possible(board,y,x,n):
    
    #questa funzione restituisce la colonna
    def genera_colonne(board, i):
        return [j[i] for j in board]
    #questa funzione restituisce la riga 
    def genera_righe(board, i):
        return board[i]
    
    def genera_square(board,y,x):
        tmp = []
        for j in range((y//3)*3, (y//3 + 1)*3):
            for i in range((x//3)*3, (x//3 + 1)*3):
                tmp.append(board[j][i])
        return tmp
    
    criteria1 = n in genera_colonne(board, x)
    criteria2 = n in genera_righe(board, y)
    criteria3 = n in genera_square(board,y,x)
    
    criteria = not (criteria1 or criteria2 or criteria3)
    
    if criteria: 
        return True
    else:
        return False

#stampo la matrice
print(np.matrix(board))
print()
chiamata = 0

def solve():
    global chiamata
    global board
    
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for number in range(1,10):
                    if possible(board,y,x,number): 
                        

                        board[y][x] = number
                        chiamata += 1
                        solve()
                        #backtracking
                        board[y][x] = 0
                return 
    print("dopo la {n} chiamata".format(n=chiamata)+"\n")
    #stampo il risultato
    print(np.matrix(board))
    input("Per un'altra soluzione premere invio"+"\n")

solve()