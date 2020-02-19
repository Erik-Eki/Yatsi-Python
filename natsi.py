# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:00:15 2020

@author: Erik
"""
import random

active_score = 0
def Yatzi(dice):
    global active_score
    count = 1
    for i in range(0, 4):
        if dice[i] == dice[i + 1]:
            count += 1
    if count == 5:
        active_score += 50
        return True

def Random(dice):
    global active_score
    active_score = sum(dice)

def Täyskäsi(dice):
    global active_score
    dice = sorted(set(dice))
    if len(dice) == 2:
        print('Fullhouse!')
        active_score += 25
        return True
    else:
        return False
    
def Pari(dice):
    global active_score
    for i in dice:
        if dice.count(i) >= 2:
            print('Matched 2 of a kind!')
            active_score += sum(dice)
            return True
        else:
            return False

def Kolme(dice):
    global active_score
    for i in dice:
        if dice.count(i) >= 3:
            print('Matched 3 of a kind!')
            active_score += sum(dice)
            return True
        else:
            return False
        
def Neljä(dice):
    for i in dice:
        global active_score
        if dice.count(i) >= 4:
            print('Matched 4 of a kind!')
            active_score += sum(dice)
            return True
        else:
            return False
        
def EbinSuora(dice):
    global active_score
    dice = str(sorted(dice))
    if '1, 2, 3, 4, 5' in dice:
        active_score += 15
        return True
    elif '2, 3, 4, 5, 6' in dice:
        active_score += 20
        return True
    else:
        return False

def NoScore(dice):
    active_score = Yatzi(dice)
    active_score = Random(dice)
    active_score = Täyskäsi(dice)
    active_score = Pari(dice)
    active_score = Kolme(dice)
    active_score = Neljä(dice)
    active_score = EbinSuora(dice)
    if active_score == 0:
        print('No match: 0 points.')
    return False

def rolls(dice):
    print(active_player + " dices: ", end= "")
    for i in dice:
        print(str(i)+" ", end="")
        
dice = []
for i in range(5):
    dice.append(random.randint(1,6))
        

activeList = dice
active_player = "Player 1"
while True:
    q1 = int(input("Enter 1 to start game "))
    if(q1 == 1):
        
        while True:
            rolls(dice)
            q3 = int(input("1 to rethrow and 2 to check"))
            if q3 == 1:
                reroll = input("Tell me witch dices you want to rethrow divided by space. Numbers 1-5 > ")
                reroll = reroll.split()
                for index, ch in enumerate(reroll):
                    reroll[index] = int(ch) - 1
                for index in reroll:
                    dice[index] = random.randint(1,6)
                Yatzi(dice)
                Random(dice)
                Täyskäsi(dice)
                Pari(dice)
                Kolme(dice)
                Neljä(dice)
                EbinSuora(dice)
                      
            elif q3 == 2:
                if active_player == "Player 1":
                    print("Player change...\n")
                    active_player = "Player 2"
                if active_score > 0:
                    print("Pisteet: "+ str(active_score) +"! wau ebin bisdeed!")
                else:
                    print("game over")
                    break
            #victory cheking comes here
      
        