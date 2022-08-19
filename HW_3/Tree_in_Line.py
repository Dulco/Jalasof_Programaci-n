import random

m = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

m2 = [[' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '"'],
      [' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '"'],
      ['_', '_', '_', '_', '|', '_', '_', '_', '_', '|', '_', '_', '_', '_', '"'],
      [' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '"'],
      [' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '"'],
      ['_', '_', '_', '_', '|', '_', '_', '_', '_', '|', '_', '_', '_', '_', '"'],
      [' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '"'],
      [' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '"'],
      [' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '"']]

play = True


def showlayer():
    for i in m2:
        for j in i:
            if (j == i[14]):
                print(j)
            if not (j == i[14]):
                print(j, end="")


def makemove(move):
    global bussy
    if (move == 'tl' and player == 1 and m[0][0]==0):
        m2[1][2] = 'X'
        m[0][0] = 1
    else:
        if (move == 'tl' and player == 2 and m[0][0]==0):
            m2[1][2] = 'O'
            m[0][0] = 2
        else:
            if (move == 'tl' and m[0][0]!=0):
                bussy=True

    if (move == 'tc' and player == 1 and m[0][1]==0):
        m2[1][7] = 'X'
        m[0][1] = 1
    else:
        if (move == 'tc' and player == 2 and m[0][1]==0):
            m2[1][7] = 'O'
            m[0][1] = 2
        else:
            if (move == 'tc' and m[0][1]!=0):
                bussy=True
    if (move == 'tr' and player == 1 and m[0][2]==0):
        m2[1][12] = 'X'
        m[0][2] = 1
    else:
        if (move == 'tr' and player == 2 and m[0][2]==0 ):
            m2[1][12] = 'O'
            m[0][2] = 2
        else:
            if (move == 'tr' and m[0][2]!=0):
                bussy=True
    if (move == 'ml' and player == 1 and m[1][0]==0):
        m2[4][2] = 'X'
        m[1][0] = 1
    else:
        if (move == 'ml' and player == 2 and m[1][0]==0):
            m2[4][2] = 'O'
            m[1][0] = 2
        else:
            if (move == 'ml' and m[1][0]!=0):
                bussy=True
    if (move == 'mc' and player == 1 and m[1][1]==0 ):
        m2[4][7] = 'X'
        m[1][1] = 1
    else:
        if (move == 'mc' and player == 2 and m[1][1]==0 ):
            m2[4][7] = 'O'
            m[1][1] = 2
        else:
            if (move == 'mc' and m[1][1]!=0):
                bussy=True
    if (move == 'mr' and player == 1 and m[1][2]==0):
        m2[4][12] = 'X'
        m[1][2] = 1
    else:
        if (move == 'mr' and player == 2 and m[1][2]==0):
            m2[4][12] = 'O'
            m[1][2] = 2
        else:
            if (move == 'mr' and m[1][2]!=0):
                bussy=True
    if (move == 'bl' and player == 1 and m[2][0]==0):
        m2[7][2] = 'X'
        m[2][0] = 1
    else:
        if (move == 'bl' and player == 2 and m[2][0]==0):
            m2[7][2] = 'O'
            m[2][0] = 2
        else:
            if (move == 'bl' and m[2][0]!=0):
                bussy=True
    if (move == 'bc' and player == 1 and m[2][1]==0 ):
        m2[7][7] = 'X'
        m[2][1] = 1
    else:
        if (move == 'bc' and player == 2 and m[2][1]==0):
            m2[7][7] = 'O'
            m[2][1] = 2
        else:
            if (move == 'bc' and m[2][1]!=0):
                bussy=True
    if (move == 'br' and player == 1 and m[2][2]==0):
        m2[7][12] = 'X'
        m[2][2] = 1
    else:
        if (move == 'br' and player == 2 and m[2][2]==0):
            m2[7][12] = 'O'
            m[2][2] = 2
        else:
            if (move == 'br' and m[2][2]!=0):
                bussy=True

bussy=False
player = random.randint(1, 2)
cont1 = 0
cont2 = 0
while (play):
    showlayer()
    print('Player', player, 'type your next movement')
    move = input()
    bussy=False
    if not (move!='tl' and move !='tc' and move!='tr' and move!='ml' and move != 'mc' and move!= 'mr' and move != 'bl' and move != 'bc' and move != 'br'):
        makemove(move)
        print(bussy)
        if(bussy==False):
            if (player == 1):
                player = 2
            else:
                if (player == 2):
                    player = 1
        if(bussy==True):
            print('your opponent already played here, try other boxes!')
    else:
        print('Type a valid movement "tl, tc, tr, ml, mc, mr, bl, bc, br"')
    for line in m:
        contline1 = 0
        contline2 = 0
        for s in line:
            if (s == 2):
                contline2 += 1
            else:
                if (s == 1):
                    contline1 += 1
            if (contline1 == 3):
                play = False
                showlayer()
                print('Player 1 won the game')
            else:
                if (contline2 == 3):
                    showlayer()
                    play = False
                    print('Player 2 won the game')
    contdiag2 = 0
    contdiag1 = 0
    for i in range(3):
        if (m[i][i] == 2):
            contdiag2 += 1
        else:
            if (m[i][i] == 1):
                contdiag1 += 1
    
    if (contdiag1 == 3):
        play = False
        showlayer()
        print('Player 1 won the game')
    else:
        if (contdiag2 == 3):
            showlayer()
            play = False
            print('Player 2 won the game')
    
    contdiag2 = 0
    contdiag1 = 0
    for i in range(3):
        if (m[i][2-i] == 2):
            contdiag2 += 1
        else:
            if (m[i][2-i] == 1):
                contdiag1 += 1
    
    if (contdiag1 == 3):
        play = False
        showlayer()
        print('Player 1 won the game')
    else:
        if (contdiag2 == 3):
            showlayer()
            play = False
            print('Player 2 won the game')

    for i in range(3):
        contcol1=0
        contcol2=0
        for j in range(3):
            if(m[j][i]==2):
                contcol2+=1
            else:
                if(m[j][i]==1):
                    contcol1+=1
        if (contcol1 == 3):
                play = False
                showlayer()
                print('Player 1 won the game')
        else:
            if (contcol2 == 3):
                showlayer()
                play = False
                print('Player 2 won the game') 
    salir=0
    for i in range(3):
        for j in range(3):
            if(m[i][j] != 0):
                salir+=1
    if(salir==9):
        play = False
        showlayer()
        print('Its a tie!') 
            