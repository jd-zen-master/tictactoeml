# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 20:31:28 2018

@author: jddave
This is a tic tac toe game using machine learning

A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.
Task = Playing a full game of tic-tac-toe
Performance = Probability of winning (games won / games played)
Experience = Number of games played


"""

#imports go here
import numpy as np
import random 


# setting up a class for the board
class Board:
    bSet = np.zeros([3,3],'int8')
    # 0=blank; 1=X, -1=O
    bState = int(0)
    # 0=in progress; 1=player 1; 2=player 2; 3=draw
    moveNumber = int(0)
    nextTurn1=bool("True")
    
    def DisplayBoard(self):
        print("\tA\tB\tC\n1\t",self.bSet[0,0],"\t",self.bSet[0,1],"\t",self.bSet[0,2],"\n2\t",self.bSet[1,0],"\t",self.bSet[1,1],"\t",self.bSet[1,2],"\n3\t",self.bSet[2,0],"\t",self.bSet[2,1],"\t",self.bSet[2,2])
#        print(bSet[])
        
    def CheckBoardStatus(self):
        # check for columns 
        if self.bSet[0,0]!=0 and self.bSet[0,0]==self.bSet[0,1] and self.bSet[0,1]==self.bSet[0,2] : self.bState=self.bSet[0,0]
        if self.bSet[1,0]!=0 and self.bSet[1,0]==self.bSet[1,1] and self.bSet[1,1]==self.bSet[1,2] : self.bState=self.bSet[1,0]
        if self.bSet[2,0]!=0 and self.bSet[2,0]==self.bSet[2,1] and self.bSet[2,1]==self.bSet[2,2] : self.bState= self.bSet[2,0]

        # check for rows
        if self.bSet[0,0]!=0 and self.bSet[0,0]==self.bSet[1,0] and self.bSet[1,0]==self.bSet[2,0] : self.bState= self.bSet[0,0]
        if self.bSet[0,1]!=0 and self.bSet[0,1]==self.bSet[1,1] and self.bSet[1,1]==self.bSet[2,1] : self.bState= self.bSet[0,1]
        if self.bSet[0,2]!=0 and self.bSet[0,2]==self.bSet[1,2] and self.bSet[1,2]==self.bSet[2,2] : self.bState= self.bSet[0,2]
        
        # check diagonals
        if self.bSet[0,0]!=0 and self.bSet[0,0]==self.bSet[1,1] and self.bSet[1,1]==self.bSet[2,2] : self.bState= self.bSet[0,0]
        if self.bSet[0,2]!=0 and self.bSet[0,2]==self.bSet[1,1] and self.bSet[1,1]==self.bSet[2,0] : self.bState= self.bSet[0,2]
        
        return self.bState

    def SetPosition(self,x,y,val=1):
        # check for columns 
        if self.bSet[int(x),int(y)]!=0: return 0
        self.bSet[int(x),int(y)]=val
        print("Moved "+str(val)+" to " + str(x)+str(y))
        self.DisplayBoard()

        return 1
        
    def PlayerValEntry(self):
        # check for columns 
        xy=input()
        while self.SetPosition(xy[0],xy[1],1)==0: xy=input()

    def SetAutoVal(self):
        for x in range(3):
            for y in range(3):
                if self.SetPosition(x,y,-1)!=0: return 1
        return 0

    def PlayGame(self):
        self.PlayerValEntry()
        while self.CheckBoardStatus()==0:
            self.SetAutoVal()
            if self.CheckBoardStatus()==0: self.PlayerValEntry()
        print("Winner is: "+str(self.bState))
        

class GameLog:
    gameId=int(round(random.random()*1000))
    gameResult=int(0)
    # 0=draw; -1=lost; 1=won


game=Board()
game.DisplayBoard()
game.PlayGame()

