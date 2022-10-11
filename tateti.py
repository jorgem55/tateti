#Created by Jorge Martinez
import random, os, time

uL=uC=uR=mL=mC=mR=dL=dC=dR=winner=pcPiece=piece=''
# placeList={uL:'',uC:'',uR:'',mL:'',mC:'',mR:'',dL:'',dC:'',dR:'',}

def board(uL,uC,uR,mL,mC,mR,dL,dC,dR):
    print('\t ---------------')
    print('\t| ',uL, ' | ', uC, ' | ', uR,' |')
    print('\t ---------------')
    print('\t| ',mL, ' | ', mC, ' | ', mR,' |')
    print('\t ---------------')
    print('\t| ',dL, ' | ', dC, ' | ', dR,' |')
    print('\t ---------------\n')
    
def crussesPC(): #jugada defensiva de PC
    pcPlace=''
    if (uL==uC==piece or dL==mC==piece or mR==dR==piece) and uR=='':
        pcPlace='UR'
    elif (uR==uC==piece or dR==mC==piece or dL==mL==piece) and uL=='':
        pcPlace='UL'
    elif (mR==mC==piece or dL==uL==piece) and mL=='':
        pcPlace='ML'
    elif (mL==mC==piece or uR==dR==piece) and mR=='':
        pcPlace='MR'
    elif (dR==dC==piece or mL==uL==piece or uR==mC==piece) and dL=='':
        pcPlace='DL'
    elif (dL==dC==piece or mR==uR==piece or uL==mC==piece) and dR=='':
        pcPlace='DR'
    elif (dC==mC==piece or uR==uL==piece) and uC=='':
        pcPlace='UC'
    elif (dL==dR==piece or uC==mC==piece) and dC=='':
        pcPlace='DC'
    elif (dL==uR==piece or uL==dR==piece or mR==mL==piece or uC==dC==piece) and mC=='':
        pcPlace='MC'
        
    return pcPlace
    
def start(piece):
    print('\n      ---------------------------------------------\n          >> Bienvenido a TaTeTi (TicTacToe) <<\n          -------------------------------------')
    print('                  -by JorgeMartinez-\n')
    while piece != 'X' and piece != 'O':
        piece=input('* Con que ficha quieres jugar? ( X  ó  O ): ')
        piece=piece.upper()
    if piece == 'X':
        pcPiece='O'
    else:
        pcPiece='X'
        
    return piece,pcPiece
    
def put(uL,uC,uR,mL,mC,mR,dL,dC,dR):
    place=''
    while place != 'UL' and place != 'UC' and place != 'UR' and place != 'ML' and place != 'MC' and place != 'MR' and place != 'DL' and place != 'DC' and place != 'DR':
        place = input('* Donde queres poner tu proxima ficha? [uL,uC,uR,mL,mC,mR,dL,dC,dR]: ')
        place = place.upper()
        if place == 'UL' and uL=='':
            uL=piece
        elif place == 'UC' and uC=='':
            uC=piece
        elif place == 'UR' and uR=='':
            uR=piece
        elif place == 'ML' and mL=='':
            mL=piece
        elif place == 'MC' and mC=='':
            mC=piece
        elif place == 'MR' and mR=='':
            mR=piece
        elif place == 'DL' and dL=='':
            dL=piece
        elif place == 'DC' and dC=='':
            dC=piece
        elif place == 'DR' and dR=='':
            dR=piece
        else: #Ya contiene ficha o es erroneo
            place=''
            print('\n* No es un casillero válido o ese casillero ya tiene ficha, ingrese nuevamente')    
    return uL,uC,uR,mL,mC,mR,dL,dC,dR

def get_winner(uL,uC,uR,mL,mC,mR,dL,dC,dR):
    winner=''
    if (uL==uC=='O' and uC==uR=='O') or (uL==uC=='X' and uC==uR=='X'):
        winner='Y'
    elif (mL==mC=='O' and mC==mR=='O')or (mL==mC=='X' and mC==mR=='X'):
        winner='Y'
    elif (dL==dC=='O' and dC==dR=='O')or(dL==dC=='X' and dC==dR=='X'):
        winner='Y'
    elif (uL==mL=='O' and mL==dL=='O')or(uL==mL=='X' and mL==dL=='X'):
        winner='Y'
    elif (uC==mC=='O' and mC==dC=='O')or(uC==mC=='X' and mC==dC=='X'):
        winner='Y'
    elif (uR==mR=='O' and mR==dR=='O')or(uR==mR=='X' and mR==dR=='X'):
        winner='Y'
    elif (uL==mC=='O' and mC==dR=='O')or(uL==mC=='X' and mC==dR=='X'):
        winner='Y'
    elif (uR==mC=='O' and mC==dL=='O')or(uR==mC=='X' and mC==dL=='X'):
        winner='Y'
    return winner

def game(uL,uC,uR,mL,mC,mR,dL,dC,dR):
    winner=''
    if get_winner(uL,uC,uR,mL,mC,mR,dL,dC,dR)=='Y': # ver si con esa ficha USER forma linea
        winner = '* Ganaste esta partida !!!'
    else: # sino aplicar nueva ficha de la PC
        pcPlace =''
        pcPlace=crussesPC() #jugada defensiva de PC
        if pcPlace!='':
            if pcPlace=='UL' and uL=='':
                uL=pcPiece
            elif pcPlace=='UC' and uC=='':
                uC=pcPiece
            elif pcPlace=='UR' and uR=='':
                uR=pcPiece
            elif pcPlace=='ML' and mL=='':
                mL=pcPiece
            elif pcPlace=='MC' and mC=='':
                mC=pcPiece
            elif pcPlace=='MR' and mR=='':
                mR=pcPiece
            elif pcPlace=='DL' and dL=='':
                dL=pcPiece
            elif pcPlace=='DC' and dC=='':
                dC=pcPiece
            elif pcPlace=='DR' and dR=='':
                dR=pcPiece
            else:
                pcPlace=''
        while pcPlace=='': #aplicar ficha al azar
                pcPlace = random.randrange(0,9)
                if pcPlace==0 and uL=='':
                    uL=pcPiece
                elif pcPlace == 1 and uC=='':
                    uC=pcPiece
                elif pcPlace == 2 and uR=='':
                    uR=pcPiece
                elif pcPlace == 3 and mL=='':
                    mL=pcPiece
                elif pcPlace == 4 and mC=='':
                    mC=pcPiece
                elif pcPlace == 5 and mR=='':
                    mR=pcPiece
                elif pcPlace == 6 and dL=='':
                    dL=pcPiece
                elif pcPlace == 7 and dC=='':
                    dC=pcPiece
                elif pcPlace == 8 and dR=='':
                    dR=pcPiece
                else:
                    pcPlace=''
        if get_winner(uL,uC,uR,mL,mC,mR,dL,dC,dR) == 'Y': #ver si con nueva ficha PC forma linea
            winner = '* La PC ha ganado esta partida !!!'
		
    return winner,uL,uC,uR,mL,mC,mR,dL,dC,dR
    
    
# MAIN
if __name__ == '__main__':    
    piece,pcPiece=start(piece)    
    print('* Este es el tablero:\n')
    print('\t\t -----------------')
    print('\t\t| uL  |  uC |  uR |')
    print('\t\t -----------------')
    print('\t\t| mL  |  mC |  mR |')
    print('\t\t -----------------')
    print('\t\t| dL  |  dC |  dR |')
    print('\t\t -----------------\n')
    print('* Al azar, veamos quien empieza jugando...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('..')
    time.sleep(1)
    print('.\n')
    time.sleep(2)
    num=random.randint(1,2)
    if num==1: #'user'
        print('- Empezas vos...\n')
    elif num==2: #'pc'
        print('- Empieza la PC...\n')
        winner,uL,uC,uR,mL,mC,mR,dL,dC,dR = game(uL,uC,uR,mL,mC,mR,dL,dC,dR) #verifica ganador, sino aplica ficha de PC y vuelve a verificar
        board(uL,uC,uR,mL,mC,mR,dL,dC,dR) #imprime tablero
        
    while winner == '':
        uL,uC,uR,mL,mC,mR,dL,dC,dR=put(uL,uC,uR,mL,mC,mR,dL,dC,dR) #pide casillero al user
        if uL!=''and uC!=''and uR!=''and mL!=''and mC!=''and mR!=''and dL!=''and dC!=''and dR!='': #si el tablero esta lleno
            winner='* Has empatado esta partida... Inicia otra partida!'
        else:
            winner,uL,uC,uR,mL,mC,mR,dL,dC,dR = game(uL,uC,uR,mL,mC,mR,dL,dC,dR) #verifica ganador, sino aplica ficha de PC y vuelve a verificar
            board(uL,uC,uR,mL,mC,mR,dL,dC,dR) #imprime tablero
        if uL!='' and uC!='' and uR!='' and mL!='' and mC!='' and mR!='' and dL!='' and dC!='' and dR!='' and winner == '': #si el tablero esta lleno
            winner='* Has empatado esta partida... Inicia otra partida!'
    print(winner)
    print('* Gracias por jugar !!!\n')
    os.system("pause")
    
    
    
# def movement():
#     move1=''
#     move2=''
#     while move1 != 'UL' and move1 != 'UC' and move1 != 'UR' and move1 != 'ML' and move1 != 'MC' and move1 != 'MR' and move1 != 'DL' and move1 != 'DC' and move1 != 'DR':
#         while move2 != 'UL' and move2 != 'UC' and move2 != 'UR' and move2 != 'ML' and move2 != 'MC' and move2 != 'MR' and move2 != 'DL' and move2 != 'DC' and move2 != 'DR':
#             while move1 == move2:
#                 move1 = input('Cual es tu proximo movimiento? \n Desde... [uL,uC,uR,mL,mC,mR,dL,dC,dR]: ')
#                 move2 = input('Hacia... [uL,uC,uR,mL,mC,mR,dL,dC,dR]: ')
#             if move1 != move2:
#                 if move2 == 'UL':
#                     uL=piece
#                 elif move2 == 'UC':
#                     uC=piece
#                 elif move2 == 'UR':
#                     uR=piece
#                 elif move2 == 'ML':
#                     mL=piece
#                 elif move2 == 'MC':
#                     mC=piece
#                 elif move2 == 'MR':
#                     mR=piece
#                 elif move2 == 'DL':
#                     dL=piece
#                 elif move2 == 'DC':
#                     dC=piece
#                 else:
#                     dR=piece
#                 # asdasd
#                 if move1 == 'UL':
#                     uL=piece
#                 elif move1 == 'UC':
#                     uC=piece
#                 elif move1 == 'UR':
#                     uR=piece
#                 elif move1 == 'ML':
#                     mL=piece
#                 elif move1 == 'MC':
#                     mC=piece
#                 elif move1 == 'MR':
#                     mR=piece
#                 elif move1 == 'DL':
#                     dL=piece
#                 elif move1 == 'DC':
#                     dC=piece
#                 else:
#                     dR=piece
            
#     return (move)