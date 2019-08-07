# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 20:31:28 2018

@author: jddave
This is a tic tac toe game using machine learning
"""

#imports go here
import numpy as np


# setting up a class for the board
class Board:
    bSet = np.zeros([3,3],'int8')
    bState = int(0)
    # 0=in progress; 1=player 1; 2=player 2; 3=draw
    moveNumber = int(0)
    nextTurn1=bool("True")
    
    def DisplayBoard(self):
        print("\tA\tB\tC\n1\t",self.bSet[0,0],"\t",self.bSet[0,1],"\t",self.bSet[0,2],"\n2\t",self.bSet[1,0],"\t",self.bSet[1,1],"\t",self.bSet[1,2],"\n3\t",self.bSet[2,0],"\t",self.bSet[2,1],"\t",self.bSet[2,2])
#        print(bSet[])
        
    def CheckBoardStatus(self):
        # check for columns 
        if self.bSet[0,0]!=0 and self.bSet[0,0]==self.bSet[0,1] and self.bSet[0,1]==self.bSet[0,2] : return self.bSet[0,0]
        if self.bSet[1,0]!=0 and self.bSet[1,0]==self.bSet[1,1] and self.bSet[1,1]==self.bSet[1,2] : return self.bSet[1,0]
        if self.bSet[2,0]!=0 and self.bSet[2,0]==self.bSet[2,1] and self.bSet[2,1]==self.bSet[2,2] : return self.bSet[2,0]

        # check for rows
        if self.bSet[0,0]!=0 and self.bSet[0,0]==self.bSet[1,0] and self.bSet[1,0]==self.bSet[2,0] : return self.bSet[0,0]
        if self.bSet[0,1]!=0 and self.bSet[0,1]==self.bSet[1,1] and self.bSet[1,1]==self.bSet[2,1] : return self.bSet[0,1]
        if self.bSet[0,2]!=0 and self.bSet[0,2]==self.bSet[1,2] and self.bSet[1,2]==self.bSet[2,2] : return self.bSet[0,2]
        
        # check diagonals
        if self.bSet[0,0]!=0 and self.bSet[0,0]==self.bSet[1,1] and self.bSet[1,1]==self.bSet[2,2] : return self.bSet[0,0]
        if self.bSet[0,2]!=0 and self.bSet[0,2]==self.bSet[1,1] and self.bSet[1,1]==self.bSet[2,0] : return self.bSet[0,2]

game=Board()
game.bSet
game.DisplayBoard()
