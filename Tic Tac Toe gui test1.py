import pyautogui as gui
gui.alert('''Welcome To Tic Tac Toe

Instructions-

1) You have to choose a symbol from 'X' and 'O'.

2) Player 1 will have their choice first.

3) At each turn the player with chance must select the tile they want their symbol in.

4) The player to have 3 symbols allinged properly first wins.

5) Do not enter the same tile twice.''','Tic Tac Toe',button='Play')
game="""

1  2  3
4  5  6
7  8  9
"""
a=b=c=d=e=f=g=h=i=0
pl1=gui.prompt('Enter Player 1','Tic Tac Toe')
pl2=gui.prompt('Enter Player 2','Tic Tac Toe')
sym1=gui.confirm('Player 1 choose your symbol','Tic Tac Toe',buttons=['X','O'])
if sym1 =="X":
    sym2="O"
elif sym1 =="O":
    sym2="X"
else:
    exit()
s='Stats-\n\n '+pl1+' with symbol '+sym1+'''
 is competing against
 '''+pl2+' with symbol '+sym2
gui.alert(s,'Tic Tac Toe',button='Continue')

for j in range(0,9):
    if j%2==0:
        p1="It's you turn "+pl1+'''
 choose your tile (Enter the tile's number)
 '''+game
        til=gui.prompt(p1,'Tic Tac Toe')
        sym=sym1
    else:
        p2="It's you turn "+pl2+'''
 choose your tile (Enter the tile's number)
 '''+game
        til=gui.prompt(p2,'Tic Tac Toe')
        sym=sym2
    if til=="1":
        game=game.replace("1",sym)
        a=sym
    elif til=="2":
        game=game.replace("2",sym)
        b=sym
    elif til=="3":
        game=game.replace("3",sym)
        c=sym
    elif til=="4":
        game=game.replace("4",sym)
        d=sym
    elif til=="5":
        game=game.replace("5",sym)
        e=sym
    elif til=="6":
        game=game.replace("6",sym)
        f=sym
    elif til=="7":
        game=game.replace("7",sym)
        g=sym
    elif til=="8":
        game=game.replace("8",sym)
        h=sym
    elif til=="9":
        game=game.replace("9",sym)
        i=sym
    else:
        pass
    if a==b==c==sym1 or d==e==f==sym1 or g==h==i==sym1 or a==d==g==sym1 or b==e==h==sym1 or c==f==i==sym1 or a==e==i==sym1 or c==e==g==sym1:
        gui.alert(pl1+' won!','Tic Tac Toe')
        break
    elif a==b==c==sym2 or d==e==f==sym2 or g==h==i==sym2 or a==d==g==sym2 or b==e==h==sym2 or c==f==i==sym2 or a==e==i==sym2 or c==e==g==sym2:
        gui.alert(pl2+' won!','Tic Tac Toe')
        break
    else:
        exit()
        if i==8:
            gui.alert("It's a Tie",'Tic Tac Toe')
