# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:00:15 2020

@author: Erik & Axel
Bugeja löytyy enemmän kuin Fallout 76:sesta
"""
import random
active_score = 0 #Tästä aktiiviset pisteet siirretään score1 ja score2 riippuen kumpi pelaaja on aktiivinen
active_player = "Player 1"
Is_p1_active = True
score1 = 0
score2 = 0
dice = []
for i in range(5):
    dice.append(random.randint(1,6))
    
#Ylätaso
def Ylätaso(dice):
    global active_score
    dice .sort()
    yl = input("What dice value? 1-6? > ")
    yl = int(yl)
    if yl == 1 and 1 in dice:
            c = dice.count(1)
            active_score += c*1
    if yl == 2 and 2 in dice:
            c = dice.count(2)
            active_score += c*2
    if yl == 3 and 3 in dice:
            c = dice.count(3)
            active_score += c*3
    if yl == 4 and 4 in dice:
            c = dice.count(4)
            active_score += c*4
    if yl == 5 and 5 in dice:
            c = dice.count(5)
            active_score += c*5
    if yl == 6 and 6 in dice:
            c = dice.count(6)
            active_score += c*6
    else:
        print("Invalid: no number\n")
    


#Alataso
def Yatzi(dice):
    global active_score
    count = 1
    for i in range(0, 4):
        if dice[i] == dice[i + 1]:
            count += 1
    if count == 5:
        active_score += 50
        return True
    else:
        return False

def Random(dice):
    global active_score
    active_score += sum(dice)
    return True

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

def LyhytSuora(dice):
	global active_score
	dice = str(sorted(dice))

	if "1, 2, 3, 4" in dice:
		active_score += 30
		return True
	elif "2, 3, 4, 5" in dice:
		active_score += 30
		return True
	elif "3, 4, 5, 6" in dice:
		active_score += 30
		return True
	else:
		return False
        
def PitkäSuora(dice):
    global active_score
    dice = str(sorted(dice))
    if '1, 2, 3, 4, 5' in dice:
        active_score += 40
        return True
    elif '2, 3, 4, 5, 6' in dice:
        active_score += 40
        return True
    else:
        return False

def NoScore(dice):
    global active_score
    if active_score == 0:
        print('No match: 0 points.')
    return False

#Nopanheitto
def rolls(dice):
    print(active_player + " dices: ", end= "")
    for i in dice:
        print(str(i)+" ", end="")


def Taulukko():
    global active_score
    while True:
        taulu = ['Upper Level (1-6)', 'Yahtzee', 'Random', 'Fullhouse', '2 of a kind', '3 of a kind', '4 of a kind', 'Small Straight', 'Large Straight', 'No Score']
        print("Tables:\n")
        for i in range(len(taulu)): #Tekee hienon "taulukon" missä mukana indeksi
            print(i, end= " ")
            print(taulu[i])
        k1 = input("Where do you want to put your dices? (0-9) 'e' for exit\n")
        k1 = int(k1)
        print("Used "+taulu[k1])
        if k1 == 0:
            Ylätaso(dice)
            return False
        elif k1 == 1:
            Yatzi(dice)
            return False
        elif k1 == 2:
            Random(dice)
            return False
        elif k1 == 3:
            Täyskäsi(dice)
            return False
        elif k1 == 4:
            Pari(dice)
            return False
        elif k1 == 5:
            Kolme(dice)
            return False
        elif k1 == 6:
            Neljä(dice)
            return False
        elif k1 == 7:
            LyhytSuora(dice)
            return False
        elif k1 == 8:
            PitkäSuora(dice)
            return False
        elif k1 == 9:
            NoScore(dice)
            return False
        else:
            return True


def Peli():
    global score1
    global score2
    count = 0 #Tällä katsotaan kuinka monta kertaa pelaaja voi täyttää taulukkoaan.
    count2= 0 #Tällä katsotaan että pelaaja voi vain heittää uudet nopat vain 3 kertaa
    while count < 13: #Pelaaja pelaa 14 kertaa, ja jos onni on täydellinen, voi hän saa taulun täyteen.
        rolls(dice)
        q3 = int(input("(1) to rethrow and (2) to check\n------------------------------\n"))
        if q3 == 1 and count2 < 3:
            reroll = input("Witch dices you want to rethrow divided by space. Numbers (1-5) > ")
            reroll = reroll.split()
            for index, ch in enumerate(reroll):
                reroll[index] = int(ch) - 1
            for index in reroll:
                dice[index] = random.randint(1,6)
            rolls(dice)
            count2 = count2 + 1
            
        elif q3 == 1 and count2 == 3:
            print("\nThrows used! Press (2) to check!\n")
                          
        elif q3 == 2 or count2 > 3:
            Taulukko()
            print(str(active_player)+" points: " + str(active_score)+"\n____________________________")
            if Is_p1_active == False:
                score2 += active_score
            elif Is_p1_active == True:
                score1 += active_score
            count = count + 1
            dice.clear()
            for i in range(5):
                dice.append(random.randint(1,6))
            active_score.clear()

def tarkistus(active_score):
    global score1
    global score2
    global active_player
    global Is_p1_active
    if Is_p1_active == True:
        Is_p1_active = False
        active_player = "Player 2"
        score1 += active_score
        print("\nPlayer 1 points: " + str(score1))
        print("\nPlayer 2 points: " + str(score2))
        print("\nPlayer change...\n------------------------------")
        Peli()
    elif Is_p1_active == False:
        Is_p1_active = True
        active_player = "Player 1"
        score2 += active_score
        print("\nPlayer 1 points: " + str(score1))
        print("\nPlayer 2 points: " + str(score2))
        print("\nPlayer change...\n------------------------------")
        Peli()

def Voittaja(score1, score2):
    print("Final scores:\n")
    print("\nPlayer 1 points: " + str(score1))
    print("\nPlayer 2 points: " + str(score2))
    if score1 > score2:
        print("Pelaaja 1 voitti!")
    elif score2 > score1:
        print("Pelaaja 2 voitti!")   

print("Welcome to Shitty Yahtzee!\n-------------------------------------------\n")    
Peli()
tarkistus(active_score)
Voittaja(score1, score2)
    

#Random kikkailu ylätasolla
# =============================================================================
# dice.sort()
#     d = []
#     al = list(set(dice))
#     for x in al:
#         d.append(dice.count(x))
#     while True:
#         if 1 in al:
#             h = al.index(1)
#             al.insert(0, al.pop(h))
#             d.insert(0, d.pop(h))
#             print("Found "+str(d[0])+" one(s)! ")
#             active_score = d[0]*al[0]
#             return True
#         if 2 in al:
#             h = al.index(2)
#             al.insert(0, al.pop(h))
#             d.insert(0, d.pop(h))
#             print("Found "+str(d[0])+" two(s)! ")
#             active_score = d[0]*al[0]
#             return True
#         if 3 in al:
#             h = al.index(3)
#             al.insert(0, al.pop(h))
#             d.insert(0, d.pop(h))
#             print("Found "+str(d[0])+" three(s)! ")
#             active_score = d[0]*al[0]
#             return True
#         if 4 in al:
#             h = al.index(4)
#             al.insert(0, al.pop(h))
#             d.insert(0, d.pop(h))
#             print("Found "+str(d[0])+" four(s)! ")
#             active_score = d[0]*al[0]
#             return True
#         if 5 in al:
#             h = al.index(5)
#             al.insert(0, al.pop(h))
#             d.insert(0, d.pop(h))
#             print("Found "+str(d[0])+" five(s)! ")
#             active_score = d[0]*al[0]
#             return True
#         if 6 in al:
#             h = al.index(6)
#             al.insert(0, al.pop(h))
#             d.insert(0, d.pop(h))
#             print("Found "+str(d[0])+" six(es)! ")
#             active_score = d[0]*al[0]
#             return True
#         else:
#             return False
# =============================================================================
