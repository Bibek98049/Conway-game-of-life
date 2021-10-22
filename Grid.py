import pygame
import numpy as np


#setting the value 1 for liveneighbours and 0 for dead neighbours.
Live=1
Dead=0
Vals=[Live,Dead]

#creating the class name grid and defining __init__ function to assign value to object properties.
class Grid:
    def __init__(self , k,):
        self.board = []
        self.k = k
        
        
#defining the 8 neighbours of a cell board[i][j] using the formula provided.    
    def neighbourSum(self,i,j,):
        Total = [self.board[(i-1+self.k)%self.k][(j-1+self.k)%self.k],
            self.board[(i-1+self.k)%self.k][j],
            self.board[(i-1+self.k)%self.k][(j+1)%self.k],
            self.board[i%self.k][(j+1)%self.k],
            self.board[(i+1)%self.k][(j+1)%self.k],
            self.board[(i+1)%self.k][j],
            self.board[(i+1)%self.k][(j-1+self.k)%self.k],
            self.board[i][(j-1+self.k)%self.k]]

        
#initialising the total number of live neighbours as 0.
# giving the minmum value of 0 for live neighbour. And using operator += to increase the live by 1. Live is equal to 1 + live.     
        live = 0
        

        for Total in Total:
            if Total == 1:
                live += 1
        return live
    
# defining the next pattern of the board[i][j] as per the transition rule of game

    def nextPattern(self):
        for i in range(0, len(self.board)-1):
            for j in range(0, i):
                live = self.neighbourSum(i,j,)
                if self.board[i][j] == 1:
                    if (live < 2) or (live > 3):
                        self.board[i][j] = 0
                else:
                    if live == 3:
                        self.board[i][j] = 1

# defining the printboard to print alive neighbours as ( * ) and dead neighbours as " ".
                        
    def printBoard(self):
        for x in self.board:
            show = ""
            for y in x:
                if y == 0:
                    show += " "
                else:
                    show += "*"
            print(show)
#create function main in next file to call all this function and perform tasks.
