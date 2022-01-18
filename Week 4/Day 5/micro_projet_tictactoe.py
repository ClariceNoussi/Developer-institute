'''tableau=['', '','']
print(f'{tableau)[0]| {tableau[2]}')
    |    |
tableau={['x', '0','0}
print (f'
[tableau[o]}  |{tableau [1]} |{tableau[2]}')
X | 0 | 0
  playerx='x'
  tableau[2]=playerx
  print (f'{tableau [0])} | {tableau [1]} | {tableau[2]}')
  X  |0  |X
  tableau=['','','','','','','','','']'''
  
  #on dessine le tableau on mettant les indice de chaque case  
tab =[0, 1, 2,3, 4, 5,6,7,8] 

''' print(f'{tab[0]} | {tab[1]} | {tab[2]} ')
    0| 1| 2
    choice = input('choose the number where you want to play:')
   
    tab[int(choice[0]='x'
    print(f'{tab[0]} | {tab[1]} | {tab[2]}')
    0 |x |2'''
#fct display board
player1='x'
player2='o'

def display_board():
    board= f'''           *****************
           * {tab[0]}   | {tab[1]}  |   {tab[2]}*
           *---------------*
           * {tab[3]}   | {tab[4]}  |   {tab[5]}*
           *---------------*
           * {tab[6]}   | {tab[7]}  |   {tab[8]}*
           *****************'''

    print(board)



#definir le gagnant
def check_win():
    for n in tab:
        if tab[0]==tab[1]==tab[2]=='x':
            print(f'congratulation {player1}you are the winner')
            return True
        elif tab[0]==tab[3]==tab[6]=='x':
            print(f'congratulation'+ player1 +"you are the winner")
        elif tab[0]==tab[4]==tab[8]=='x':
            print(f'congratulation'+ player1 +"you are the winner")
        elif tab[1]==tab[4]==tab[7]=='x':
            print(f'congratulation'+ player1 +"you are the winner")
        elif tab[2]==tab[5]==tab[8]=='x':
            print(f'congratulation'+ player1 +"you are the winner")
        elif tab[2]==tab[4]==tab[6]=='x':
            print(f'congratulation'+ player1 +"you are the winner")
        elif tab[3]==tab[4]==tab[5]=='x':
            print(f'congratulation'+ player1 +"you are the winner")
        elif tab[6]==tab[7]==tab[8]=='x':
            print(f'congratulation'+ player1 +"you are the winner")
            #joueur 2
        elif tab[0]==tab[1]==tab[2]=='o':
            print('congratulation '+ player2+ 'you are the winner')
        elif tab[0]==tab[3]==tab[6]=='o':
            print('congratulation '+ player2+ 'you are the winner')
        elif tab[0]==tab[4]==tab[8]=='o':
            print('congratulation '+ player2+ 'you are the winner')
        elif tab[1]==tab[4]==tab[7]=='o':
            print('congratulation '+ player2+ 'you are the winner')
        elif tab[2]==tab[5]==tab[8]=='o':
            print('congratulation '+ player2+ 'you are the winner')
        elif tab[2]==tab[4]==tab[6]=='o':
            print('congratulation '+ player2+ 'you are the winner')
        elif tab[3]==tab[4]==tab[5]=='o':
            print('congratulation '+ player2+ 'you are the winner')
        elif tab[6]==tab[7]==tab[8]=='o':
            print('congratulation '+ player2+ 'you are the winner')
            
#fct player input

def player_input(player):
    jeu = int(input('choose the number where you want to play '))
    tab[int(jeu)]= player
    display_board()
    return check_win()



#fction play
def play():
    print('WELCOME TO TIC TAC TOE\n')
    print('TIC TAC TOE \n')
    display_board()
    for tours in range (0-9):
        if tours%2==0:
            print(f'C est le tour de {player1}') #on me demande d'entrer un nombre, ensuite on dit c'est le tour de x donc on a 2 fois x avant 0
            win= player_input(player1)
            player_input(player1)
            display_board()
            if win:
                print ('End of game')
                break
        else:
            print(f'C est le tour de {player2}' )
            player_input(player2)
            display_board()
    else:
        print('No one won, Goodbye')

play()