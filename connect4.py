#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 18:39:48 2019

@author: willdarden
"""




# game board
import random
from Connect4Board import Board
from Connect4Player import Player
from Connect4Piece import Piece
config = {
        "team1Char": 'X',
        "team2Char": 'O'
        }


class C4:
    history = []
    players = []
    rate = .5
    def __init__(self, nPlayers=100):
        for i in range(nPlayers):
            self.players.append(Player(str(int(random.random()*1000))))
#        self.players.append(Player(config['team2Char']))

    def printHistory(self):
        for h in self.history:
            print(h)

    def printWinners(self):
        splayers = sorted(self.players, reverse=True,key=lambda p: p.wins/max(.00001,p.total))
        for p in splayers:
            print(p.team, 'wins', p.wins, 'total', p.total, 'loss', p.losses, 'percentage', p.wins/p.total)
    def evolve(self, top=None):
        if top == None:
            top = self.rate
        splayers = sorted(self.players, reverse=True,key=lambda p: p.wins/max(.00001,p.total))
#        for p in splayers:
#            print(p.team, 'wins', p.wins, 'total', p.total, 'loss', p.losses)
        for i in range(int(len(splayers)/2)):
            splayers[-1 + (i * -1)] = splayers[i].mutate()
        
    def runGame(self, p1, p2, printGame=False):
        b = Board([7,6], [p1,p2])
        winner = b.hasWinner()
        nMoves = 0
        while winner == None and b.availableMoves():
            p1Moved = False
            while not p1Moved:
                move = p1.move(b)
                p1Moved = b.dropPiece(move, Piece(p1.team))
            winner = b.hasWinner() 
            if b.availableMoves() and not winner:
                p2Moved = False
                while not p2Moved:
                    move = p2.move(b)
                    p2Moved = b.dropPiece(move, Piece(p2.team))
            winner = b.hasWinner()
            nMoves += 1
        result = {"result": 0, "nMoves": nMoves}
        if winner is not None:
            if winner.team == p1.team:
                p1.wins += 1
                p1.total += 1
                p2.losses += 1
                p2.total += 1
            else:
                p2.wins += 1
                p2.total += 1
                p1.losses += 1
                p1.total += 1
            result = {"result": 1 if winner.team == p1.team else -1, "nMoves": nMoves}
        if printGame:
            b.printBoard()
        self.history.append(result)
        return winner
               
    def runTournament(self, rounds=10, printGame = False):
        for i in range(rounds):
            p1i = int(random.random() * len(self.players))
            p2i = int(random.random() * len(self.players))
            if (p1i == p2i):
                p2i = int(random.random() * len(self.players))
            p1 = self.players[p1i]
            p2 = self.players[p2i]
            self.runGame(p1, p2, printGame)
        self.evolve()

    def setThreshold(self, rate=.5):
        self.rate = rate
    def printPlayers(self):
        for p in self.players:
            print(p.team)












