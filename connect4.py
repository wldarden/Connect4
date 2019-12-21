#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 18:39:48 2019

@author: willdarden
"""




# game board

import random

config = {
        "team1Char": 'X',
        "team2Char": 'O'
        }


class Board:
    board = [[None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None]]
    
    def printBoard(self):
        rowNumber = 0
        print('*****************************')
        print('Column', [' 0 ', ' 1 ', ' 2 ', ' 3 ', ' 4 ',' 5 ',' 6 '])
        for row in self.board:
            strRow = []
            for p in row:
                if p is None:
                    strRow.append('   ')
                else:
                    strRow.append(' ' + p.team + ' ')
            print('Row:', rowNumber, strRow)
            rowNumber += 1
        print('*****************************')
            
    def dropPiece(self, col, piece):
        for ri in range(len(self.board) - 1, -1, -1):
            if (self.board[ri][col] is None):
                self.board[ri][col] = piece
                return True
        print('Error, column filled')
        raise

    """Returns None if no winner, returns team if a win is found"""
    def hasWinner(self):
        #check row:
        for row in self.board:
            aCount = 0
            bCount = 0
            for pos in row:
                if pos == None:
                    aCount = 0
                    bCount = 0
                else:
                    if pos.team == config['team1Char']:
                        aCount += 1
                        bCount = 0
                    elif pos.team == config['team2Char']:
                        aCount = 0
                        bCount += 1                    
                    if aCount >= 4:
                        return config['team1Char']
                    elif bCount >= 4:
                        return config['team2Char']
        # check Columns
        for c in range(len(self.board[0])):
            aCount = 0
            bCount = 0
            for row in self.board:
                pos = row[c]
                if pos == None:
                    aCount = 0
                    bCount = 0
                else:
                    if pos.team == config['team1Char']:
                        aCount += 1
                        bCount = 0
                    elif pos.team == config['team2Char']:
                        aCount = 0
                        bCount += 1                    
                    if aCount >= 4:
                        return config['team1Char']
                    elif bCount >= 4:
                        return config['team2Char']
        #check diagonals
        for rowi in range(len(self.board) - 1,0, -1):
            for coli in range(len(self.board[0])):
                if self.board[rowi][coli] is not None:
                    piece = self.board[rowi][coli]
                    #check left
                    isWin = self.checkDiagonal(1, rowi, coli, piece, -1)
                    if isWin is not None:
                        return piece.team
                    #check right
                    isWin = self.checkDiagonal(1, rowi, coli, piece, 1)
                    if isWin is not None:
                        return piece.team
        #if weve gotten here, there is no winner.
        return None

    """Returns None if diagonal is not a win, returns team if is a win"""
    def checkDiagonal(self, run, row, col, piece, direction):
        if run >= 4:
            return piece.team
        if ((col + direction) < 0) or ((col + direction) > len(self.board[0])):
            return None
        if row < 0 or row > len(self.board):
            return None
        team = piece.team
        if self.board[row-1][col + direction] is not None and self.board[row-1][col + direction].team == team:
            return self.checkDiagonal(run + 1, row - 1, col + direction, piece, direction)
        else:
            return None
        

class Piece:
    team = ''
    
    def __init__(self, team):
        self.team = team

               
class Player:
    
    def move(self, board=[]):
        return random.random()



b = Board()
b.printBoard()
b.dropPiece(4, Piece(config['team1Char']))

b.dropPiece(3, Piece(config['team2Char']))
b.dropPiece(3, Piece(config['team1Char']))

b.dropPiece(2, Piece(config['team2Char']))
b.dropPiece(2, Piece(config['team2Char']))
b.dropPiece(2, Piece(config['team1Char']))

b.dropPiece(1, Piece(config['team2Char']))
b.dropPiece(1, Piece(config['team2Char']))
b.dropPiece(1, Piece(config['team2Char']))
b.dropPiece(1, Piece(config['team1Char']))
#b.dropPiece(3, Piece(config['team1Char']))
#b.dropPiece(3, Piece(config['team1Char']))
b.printBoard()
winner = b.hasWinner()
if (winner):
    print('Winner!', winner)
else:
    print('No Winner')
b.printBoard()


















