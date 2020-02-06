# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:00:15 2020

@author: Erik
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:17:30 2020

@author: zbook
"""
      
    

def Yatzi(dice):
    score = 0
    count = 1
    for i in range(0, 4):
        if dice[i] == dice[i + 1]:
            count += 1
    if count == 5:
        score = 50
        return score
    else:
        return score

def Random(dice):
    score = sum(dice)
    return score

def Täyskäsi(dice):
    score = 0
    dice = sorted(set(dice))
    if len(dice) == 2:
        score = 25
        return score
    else:
        return score