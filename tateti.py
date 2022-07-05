#Created by Jorge Martinez
import random, os

uL=uC=uR=mL=mC=mR=dL=dC=dR=winner=pcPiece=piece=''
# placeList={uL:'',uC:'',uR:'',mL:'',mC:'',mR:'',dL:'',dC:'',dR:'',}

def board(uL,uC,uR,mL,mC,mR,dL,dC,dR):
    print('\n --------------')
    print('| ',uL, ' | ', uC, ' | ', uR,' |')
    print(' --------------')
    print('| ',mL, ' | ', mC, ' | ', mR,' |')
    print(' --------------')
    print('| ',dL, ' | ', dC, ' | ', dR,' |')
    print(' --------------\n')
    
def inicio(piece):
    print('\n      ----------------------------------\n          >> Bienvenido a TaTeTi <<\n          --------------------------')
    print('         >> Welcome to TicTacToe <<\n      ----------------------------------\n              -by JorgeMartinez-\n')
    while piece != 'X' and piece != 'O':
        piece=input('** Con que ficha quieres jugar? ( X  ó  O ): ')
        piece=piece.upper()
    if piece == 'X':
        pcPiece='O'
    else:
        pcPiece='X'
        
    return piece,pcPiece
    
def put(uL,uC,uR,mL,mC,mR,dL,dC,dR):
    place=''
    while place != 'uL' and place != 'uC' and place != 'uR' and place != 'mL' and place != 'mC' and place != 'mR' and place != 'dL' and place != 'dC' and place != 'dR':
        place = input('** Donde queres poner tu proxima ficha? [uL,uC,uR,mL,mC,mR,dL,dC,dR]: ')
        if place == 'uL' and uL=='':
            uL=piece
        elif place == 'uC' and uC=='':
            uC=piece
        elif place == 'uR' and uR=='':
            uR=piece
        elif place == 'mL' and mL=='':
            mL=piece
        elif place == 'mC' and mC=='':
            mC=piece
        elif place == 'mR' and mR=='':
            mR=piece
        elif place == 'dL' and dL=='':
            dL=piece
        elif place == 'dC' and dC=='':
            dC=piece
        elif place == 'dR' and dR=='':
            dR=piece
        else: #Ya contiene ficha o erroneo
            place=''
            print('\n** No es un casillero válido o ese casillero ya tiene ficha, ingrese otro')
    
    return uL,uC,uR,mL,mC,mR,dL,dC,dR

def get_winner(uL,uC,uR,mL,mC,mR,dL,dC,dR):
    winner=''
    
    if (uL==uC=='O' and uC==uR=='O')or(uL==uC=='X' and uC==uR=='X'):
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
        winner = 'Vos'
    else: # sino aplicar nueva ficha de la PC
        pcPlace =''
        while pcPlace=='': 
            pcPlace = random.randrange(0,9)
            if pcPlace == 0 and uL=='':
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
            elif uL!=''and uC!=''and uR!=''and mL!=''and mC!=''and mR!=''and dL!=''and dC!=''and dR!='': #si el tablero esta todo ocupado
                pcPlace='tie'
            else:
                pcPlace=''
        #ver si con nueva ficha PC forma linea
        if get_winner(uL,uC,uR,mL,mC,mR,dL,dC,dR) == 'Y':
            winner = 'La PC'
            if winner=='' and pcPlace=='tie':
                winner = 'tie'
		
    return winner,uL,uC,uR,mL,mC,mR,dL,dC,dR
    
    
# MAIN
if __name__ == '__main__':    
    piece,pcPiece=inicio(piece)    
    print('** Este es el tablero... \n')
    print(' -----------------')
    print('| uL  |  uC |  uR |')
    print(' -----------------')
    print('| mL  |  mC |  mR |')
    print(' -----------------')
    print('| dL  |  dC |  dR |')
    print(' -----------------\n')
    while winner == '':
        #pide casillero al user
        uL,uC,uR,mL,mC,mR,dL,dC,dR=put(uL,uC,uR,mL,mC,mR,dL,dC,dR) 
        # movement()
        #verifica ganador, sino aplica ficha de PC y vuelve a verificar
        winner,uL,uC,uR,mL,mC,mR,dL,dC,dR = game(uL,uC,uR,mL,mC,mR,dL,dC,dR) 
        #imprime tablero
        board(uL,uC,uR,mL,mC,mR,dL,dC,dR) 
        
    if winner == 'tie':
        print('** Has empatado esta partida\n ** Inicia otra partida')
    else:                    
        print('**',winner, 'ha/s ganado esta partida !!!')
    print('** Gracias por jugar !!!\n')
    os.system("pause")
    
    
    
    
    
# def movement():
#     move1=''
#     move2=''
#     while move1 != 'uL' and move1 != 'uC' and move1 != 'uR' and move1 != 'mL' and move1 != 'mC' and move1 != 'mR' and move1 != 'dL' and move1 != 'dC' and move1 != 'dR':
#         while move2 != 'uL' and move2 != 'uC' and move2 != 'uR' and move2 != 'mL' and move2 != 'mC' and move2 != 'mR' and move2 != 'dL' and move2 != 'dC' and move2 != 'dR':
#             while move1 == move2:
#                 move1 = input('Cual es tu proximo movimiento? \n Desde... [uL,uC,uR,mL,mC,mR,dL,dC,dR]: ')
#                 move2 = input('Hacia... [uL,uC,uR,mL,mC,mR,dL,dC,dR]: ')
#             if move1 != move2:
#                 if move2 == 'uL':
#                     uL=piece
#                 elif move2 == 'uC':
#                     uC=piece
#                 elif move2 == 'uR':
#                     uR=piece
#                 elif move2 == 'mL':
#                     mL=piece
#                 elif move2 == 'mC':
#                     mC=piece
#                 elif move2 == 'mR':
#                     mR=piece
#                 elif move2 == 'dL':
#                     dL=piece
#                 elif move2 == 'dC':
#                     dC=piece
#                 else:
#                     dR=piece
#                 # asdasd
#                 if move1 == 'uL':
#                     uL=piece
#                 elif move1 == 'uC':
#                     uC=piece
#                 elif move1 == 'uR':
#                     uR=piece
#                 elif move1 == 'mL':
#                     mL=piece
#                 elif move1 == 'mC':
#                     mC=piece
#                 elif move1 == 'mR':
#                     mR=piece
#                 elif move1 == 'dL':
#                     dL=piece
#                 elif move1 == 'dC':
#                     dC=piece
#                 else:
#                     dR=piece
            
#     return (move)