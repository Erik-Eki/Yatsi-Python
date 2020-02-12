# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:00:15 2020

@author: Erik
"""
score1=0
active_score = 0
def Yatzi(dice):
    global score1
    global score2
    count = 1
    for i in range(0, 4):
        if dice[i] == dice[i + 1]:
            count += 1
    if count == 5:
        score1 += 50
        score2 += 50
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
       
import random as rnd
player1_dices = [0,0,0,0,0]
def spinDices(l: list,i):
    l[i] = rnd.randint(1,6)
    player1_dices.sort()
def first_dice(l:list):
    for i in range(0,5):
        l[i] = (rnd.randint(1,6))
        

activeList = player1_dices
active_player = "Player1"
while True:
    q1 = int(input("Enter 1 to start game "))
    if(q1 == 1):
        first_dice(player1_dices)
        
        while True:
            print(active_player +  " dices: " + str(activeList))
            q3 = int(input("Do you want to rethrow or enter thingyma \n 1 to rethrow and 2 to enter thingyma thing"))
            if q3 == 1:
                  q2 = input("Tell me witch dices you want to rethrow divided by space. Numbers 0-4 ")
                  for item in q2.split():
                      spinDices(activeList, int(item))
                      print(activeList)
                      dice = activeList
                      Yatzi(dice)
                      Random(dice)
                      Täyskäsi(dice)
                      Pari(dice)
                      Kolme(dice)
                      Neljä(dice)
                      EbinSuora(dice)
                      
            elif q3 == 2:
                q4 = int(input('Enter what you want: \n 1. \n 2. \n 3. \n 4. \n 5. \n 6. \n 7. \n 8.'))
            #victory cheking comes here
      
        