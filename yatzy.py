import random
filename=("Yatzy_High_score.txt")
active_score = 0


def readHighScore():
    of=open(filename, 'r')
    for read in of:
        print("Last score: ",read, ".\n")
    of.close()
    
nopat=[]
def throw_nopat():    
    eka = random.randint(1, 6) 
    nopat.append(eka)
    toka = random.randint(1,6)
    nopat.append(toka)
    kolmas = random.randint(1,6)
    nopat.append(kolmas)
    neljäs= random.randint(1,6)
    nopat.append(neljäs)
    viides = random.randint(1,6)
    nopat.append(viides)
def first_rethrow():
        nv=input("Valitse nopat, mitkä haluat heittää uudelleen. Voit heittä kaikkia noppia uudelleen.")
        first=[]
        firstdie=nv.split()
        for l in firstdie:
            first.append(int(l))
        if nv=='':
            second_rethrow()
        else:
            for idx in first:
                nopat[idx]=random.randint(1, 6)
            print(nopat)
def second_rethrow():
    nv=input("Valitse nopat, mitkä haluat heittää uudelleen. Voit heittä kaikkia noppia uudelleen.")
    first=[]
    firstdie=nv.split()
    for l in firstdie:
        first.append(int(l))
    if nv=='':
        score()
    else:
        for idx in first:
            nopat[idx]=random.randint(1, 6)
    print(nopat)       

def score():
    score=(sum(nopat))
    str(score)
    wf=open(filename, 'w')
    wf.write(str(score))
    print("Pisteesi on: ",score,".")


def Yatzi(nopat):
    count = 1
    for i in range(0, 4):
        if nopat[i] == nopat[i + 1]:
            count += 1
    if count == 5:
        return True

def Random(nopat):
    global active_score


def Täyskäsi(nopat):
    global active_score
    nopat = sorted(set(nopat))
    if len(nopat) == 2:
        print('1. Fullhouse!')
       
        return True
    else:
        return False
    
def Pari(nopat):
    global active_score
    for i in nopat:
        if nopat.count(i) >= 2:
           print("2. Two of a kind")
           return True
        else:
            return False

def Kolme(nopat):
    global active_score
    for i in nopat:
        if nopat.count(i) >= 3:
            print("3. 3 of a kind")
            return True
        else:
            return False
        
def Neljä(nopat):
    for i in nopat:
        global active_score
        if nopat.count(i) >= 4:
            print('4. Matched 4 of a kind!')
          
            return True
        else:
            return False
        
def EbinSuora(nopat):
    global active_score
    nopat = str(sorted(nopat))
    if '1, 2, 3, 4, 5' in nopat:
        print('5. Got a straight!')
        return True
    elif '2, 3, 4, 5, 6' in nopat:
        return True
    else:
        return False

def NoScore(nopat):
    if active_score == 0:
        print('No match: 0 points.')
        return False

def tarkistus():
    global active_score
    Yatzi(nopat)
    Random(nopat)
    Täyskäsi(nopat)
    Pari(nopat)
    Kolme(nopat)
    Neljä(nopat)
    EbinSuora(nopat)
    valinta=int(input("Minkä valitset?"))
    if (valinta == 1):
         active_score += 25
         print("Fullhouse! Pisteesi on: ", active_score)
    if (valinta==2):
        active_score += sum(nopat)
        print('2. Matched 2 of a kind!', active_score)
    if (valinta == 3):
        active_score += sum(nopat)
        print('3. Matched 3 of a kind!', active_score)
    if (valinta == 4):
        active_score += sum(nopat)
        print('4. Matched 4 of a kind!', active_score)
    if (valinta == 5):
        active_score += 15
        print(' 5. Got a straight!', active_score)
    if (active_score == 0):
        active_score += 0
        print('No match: 0 points')
def play_game():
    readHighScore()
    throw_nopat()
    print(nopat)
    first_rethrow()
    second_rethrow()
    tarkistus()
    print("Peli loppui.")
    
play_game()