#Created by Jorge Martinez
import random, os, time, sys
from tkinter import DISABLED, Tk, Label, Button
from tkinter import messagebox as mb

place=pcPlace=0
uL=uC=uR=mL=mC=mR=dL=dC=dR=winner=pcPiece=piece=ficha=pcUserPiece=pcUserPlace=''

def quit():
    respuesta=mb.askyesno("Atención", "¿Quiere salir del programa?")
    if respuesta==True:
        sys.exit()

def screenConfig():
    root.title("TicTacToe")
    # Obtienes el ancho de la pantalla con root.winfo_screenwidth() y lo divides en dos, obteniendo sólo la parte entera, a lo que le restas la mitad del ancho de tu ventana. Lo mismo aplica para el alto, pero usando root.winfo_screenheight(). Luego concatenas los datos para formar la cadena que espera geometry
    wtotal = root.winfo_screenwidth()
    htotal = root.winfo_screenheight()
    wScreen=round(wtotal/2 - 225/2)
    hScreen=round(htotal/2 - 380/2)
    root.geometry(str(225)+"x"+str(380)+"+"+str(wScreen)+"+"+str(hScreen))

def get_winner():
    global uL,uC,uR,mL,mC,mR,dL,dC,dR,winner,piece
    winner=''
    # Si hay tateti asigna ficha ganadora
    if (uL==uC=='O' and uC==uR=='O') or (mL==mC=='O' and mC==mR=='O') or (dL==dC=='O' and dC==dR=='O') or (uL==mL=='O' and mL==dL=='O') or (uC==mC=='O' and mC==dC=='O') or (uR==mR=='O' and mR==dR=='O') or (uL==mC=='O' and mC==dR=='O') or (uR==mC=='O' and mC==dL=='O'):
        winner='O'
    elif (uL==uC=='X' and uC==uR=='X') or (mL==mC=='X' and mC==mR=='X') or (dL==dC=='X' and dC==dR=='X') or (uL==mL=='X' and mL==dL=='X') or (uC==mC=='X' and mC==dC=='X') or (uR==mR=='X' and mR==dR=='X') or (uL==mC=='X' and mC==dR=='X') or (uR==mC=='X' and mC==dL=='X'):
        winner='X'

    if winner!='':
        # ver si con esa ficha USER forma linea
        if piece==winner:
            winner = '* Ganaste esta partida !!!'
        else:
            #ver si con nueva ficha PC forma linea
            winner = '* La PC ha ganado esta partida !!!'
    elif uL!='' and uC!='' and uR!='' and mL!='' and mC!='' and mR!='' and dL!='' and dC!='' and dR!='' and winner == '': 
        #si el tablero esta lleno
        winner='* Has empatado esta partida... Inicia otra!!!'

    if winner!='':
        mb.showinfo("Info",winner)
        mb.showinfo("Goodbye!","Gracias por jugar !!!")
        root.destroy()

def buttonAfter(btn,pcUserPiece):
    btn['text']=pcUserPiece
    btn["state"]=DISABLED
    if pcUserPiece=='X':
        btn["bg"]="lightblue"
    else:
        btn["bg"]="lightgreen"

def changeButton(pcUserPlace,pcUserPiece):
    global uL,uC,uR,mL,mC,mR,dL,dC,dR
    if pcUserPlace == 1 and uL==pcUserPiece:
        buttonAfter(btn1,pcUserPiece)
    elif pcUserPlace == 2 and uC==pcUserPiece:
        buttonAfter(btn2,pcUserPiece)
    elif pcUserPlace == 3 and uR==pcUserPiece:
        buttonAfter(btn3,pcUserPiece)
    elif pcUserPlace == 4 and mL==pcUserPiece:
        buttonAfter(btn4,pcUserPiece)
    elif pcUserPlace == 5 and mC==pcUserPiece:
        buttonAfter(btn5,pcUserPiece)
    elif pcUserPlace == 6 and mR==pcUserPiece:
        buttonAfter(btn6,pcUserPiece)
    elif pcUserPlace == 7 and dL==pcUserPiece:
        buttonAfter(btn7,pcUserPiece)
    elif pcUserPlace == 8 and dC==pcUserPiece:
        buttonAfter(btn8,pcUserPiece)
    elif pcUserPlace == 9 and dR==pcUserPiece:
        buttonAfter(btn9,pcUserPiece)
    else: #Ya contiene ficha o es erroneo
        mb.showinfo("Info","No se cambio apariencia")
    get_winner()

def crussesPC():
    global pcPlace,uL,uC,uR,mL,mC,mR,dL,dC,dR,pcPiece,piece
    #jugada defensiva de PC
    pcPlace=0
    if (uL==uC==piece or dL==mC==piece or mR==dR==piece) and uR=='':
        pcPlace=3
    elif (uR==uC==piece or dR==mC==piece or dL==mL==piece) and uL=='':
        pcPlace=1
    elif (mR==mC==piece or dL==uL==piece) and mL=='':
        pcPlace=4
    elif (mL==mC==piece or uR==dR==piece) and mR=='':
        pcPlace=6
    elif (dR==dC==piece or mL==uL==piece or uR==mC==piece) and dL=='':
        pcPlace=7
    elif (dL==dC==piece or mR==uR==piece or uL==mC==piece) and dR=='':
        pcPlace=9
    elif (dC==mC==piece or uR==uL==piece) and uC=='':
        pcPlace=2
    elif (dL==dR==piece or uC==mC==piece) and dC=='':
        pcPlace=8
    elif (dL==uR==piece or uL==dR==piece or mR==mL==piece or uC==dC==piece) and mC=='':
        pcPlace=5
        
    # jugada inicial de PC
    while pcPlace==0:
        pcPlace = random.randrange(1,10)
        if (pcPlace==1 and uL!='') or (pcPlace==2 and uC!='') or (pcPlace==3 and uR!='') or (pcPlace==4 and mL!='') or (pcPlace==5 and mC!='') or (pcPlace==6 and mR!='') or (pcPlace==7 and dL!='') or (pcPlace==8 and dC!='') or (pcPlace==9 and dR!=''):
            pcPlace=0

    # asignar ficha a variable
    if pcPlace!=0:
        if pcPlace==1 and uL=='':
            uL=pcPiece
        elif pcPlace==2 and uC=='':
            uC=pcPiece
        elif pcPlace==3 and uR=='':
            uR=pcPiece
        elif pcPlace==4 and mL=='':
            mL=pcPiece
        elif pcPlace==5 and mC=='':
            mC=pcPiece
        elif pcPlace==6 and mR=='':
            mR=pcPiece
        elif pcPlace==7 and dL=='':
            dL=pcPiece
        elif pcPlace==8 and dC=='':
            dC=pcPiece
        elif pcPlace==9 and dR=='':
            dR=pcPiece
    changeButton(pcPlace,pcPiece)

def putPiece():
    global place,uL,uC,uR,mL,mC,mR,dL,dC,dR,piece
    if place == 1 and uL=='':
        uL=piece
    elif place == 2 and uC=='':
        uC=piece
    elif place == 3 and uR=='':
        uR=piece
    elif place == 4 and mL=='':
        mL=piece
    elif place == 5 and mC=='':
        mC=piece
    elif place == 6 and mR=='':
        mR=piece
    elif place == 7 and dL=='':
        dL=piece
    elif place == 8 and dC=='':
        dC=piece
    elif place == 9 and dR=='':
        dR=piece
    else: #Ya contiene ficha o es erroneo
        mb.showinfo("Info","No se puede elegir casillero ocupado con una ficha")
    changeButton(place,piece)
    
def game1():
    global place,uL,uC,uR,mL,mC,mR,dL,dC,dR,piece
    place=1 #To Test
    putPiece()
    crussesPC() #aplicar nueva ficha de la PC -jugada defensiva-
    
def game2():
    global place,uL,uC,uR,mL,mC,mR,dL,dC,dR,piece
    place=2 #To Test
    putPiece()
    crussesPC() #aplicar nueva ficha de la PC -jugada defensiva-
    
def game3():
    global place,uL,uC,uR,mL,mC,mR,dL,dC,dR,piece
    place=3 #To Test
    putPiece()
    crussesPC() #aplicar nueva ficha de la PC -jugada defensiva-
        
def game4():
    global place,uL,uC,uR,mL,mC,mR,dL,dC,dR,piece
    place=4 #To Test
    putPiece()
    crussesPC() #aplicar nueva ficha de la PC -jugada defensiva-
        
def game5():
    global place,uL,uC,uR,mL,mC,mR,dL,dC,dR,piece
    place=5 #To Test
    putPiece()
    crussesPC() #aplicar nueva ficha de la PC -jugada defensiva-
        
def game6():
    global place,uL,uC,uR,mL,mC,mR,dL,dC,dR,piece
    place=6 #To Test
    putPiece()
    crussesPC() #aplicar nueva ficha de la PC -jugada defensiva-
        
def game7():
    global place
    place=7 #To Test
    putPiece()
    crussesPC() #aplicar nueva ficha de la PC -jugada defensiva-
        
def game8():
    global place
    place=8 #To Test
    putPiece()
    crussesPC() #aplicar nueva ficha de la PC -jugada defensiva-
        
def game9():
    global place
    place=9 #To Test
    putPiece()
    crussesPC() #aplicar nueva ficha de la PC -jugada defensiva-
    
# def ficha():
#     top=Toplevel()
#     top.title("Ficha")
#     piece=""
#     while piece != 'X' and piece != 'O':
#         lbl=Label(top, text="Con que ficha quieres jugar?  X  ó  O ")
#         lbl.pack(side=LEFT)
#         # lbl.grid(row=0,column=1, pady=18, ipadx=15, ipady=8)
#         ficha=Entry(top)
#         ficha.pack(side=RIGHT)
#         #ficha.grid(row=2,column=1, pady=18, ipadx=15, ipady=8)
#         # str()
#         # ficha.place(x=1,y=4)
#         # ficha.place(relx=3,rely=1, relwidth=2, relheight=1)
#         #if ficha.get() == 'X':
#         # piece=ficha
#         # piece=piece.upper()
#     root.mainloop()
#     if piece == 'X':
#         pcPiece='O'
#     else:
#         pcPiece='X'
#     return piece

# def ig():
#     os.abort
# mygoogle = Button(root,text="IG",bg="gray",fg="black", command=ig).pack(pady=50)

if __name__ == '__main__':
    root = Tk()
    screenConfig()

    #fila 0
    lbl1=Label(root,text=">> Ta Te Ti <<\n-by JorgeMartinez-\n")
    lbl1.grid(row=0, columnspan=7, padx=1, pady=13, ipadx=45, ipady=1)

    screenConfig()
    #actualizar GUI
    root.update_idletasks()
    root.update()
    
    lbl2=Label(root,text=".", fg="red")
    lbl2.grid(row=1,column=0, padx=1, pady=1, ipadx=3, ipady=1)
    #fila 1
    #lambda: ficha='1'
    btn1=Button(root, text="1", bg="lightgray",fg="darkgray", command=game1)
    btn2=Button(root,text="2", bg="lightgray",fg="darkgray", command=game2)
    btn3=Button(root,text="3", bg="lightgray",fg="darkgray", command=game3)
    btn1.grid(row=1,column=1, padx=1, pady=8, ipadx=15, ipady=8)
    btn2.grid(row=1,column=2, padx=1, pady=8, ipadx=15, ipady=8)
    btn3.grid(row=1,column=3, padx=1, pady=8, ipadx=15, ipady=8)

    lbl2.grid(row=2,column=0, padx=1, pady=1, ipadx=3, ipady=1)
    #fila 2
    btn4=Button(root,text="4", bg="lightgray",fg="darkgray", command=game4)
    btn5=Button(root,text="5", bg="lightgray",fg="darkgray", command=game5)
    btn6=Button(root,text="6", bg="lightgray",fg="darkgray", command=game6)
    btn4.grid(row=2,column=1, padx=3, pady=8, ipadx=15, ipady=8)
    btn5.grid(row=2,column=2, padx=3, pady=8, ipadx=15, ipady=8)
    btn6.grid(row=2,column=3, padx=3, pady=8, ipadx=15, ipady=8)
    
    lbl2.grid(row=3,column=0, padx=1, pady=8, ipadx=3, ipady=1)
    #fila 3
    btn7=Button(root,text="7", bg="lightgray",fg="darkgray", command=game7)
    btn8=Button(root,text="8", bg="lightgray",fg="darkgray", command=game8)
    btn9=Button(root,text="9", bg="lightgray",fg="darkgray", command=game9)
    btn7.grid(row=3,column=1, padx=3, pady=8, ipadx=15, ipady=8)
    btn8.grid(row=3,column=2, padx=3, pady=8, ipadx=15, ipady=8)
    btn9.grid(row=3,column=3, padx=3, pady=8, ipadx=15, ipady=8)

    #fila 4 - Exit
    btn0=Button(root,text="Exit",bg="black",fg="white", command=quit)
    btn0.grid(row=4,column=2, padx=10, pady=10, ipadx=16, ipady=8)

    #root.withdraw() #Ocultar ventana principal
    mb.showinfo("Info","* Al azar, veamos con que ficha jugaras (X  ó  O) y quien empieza jugando...")
    time.sleep(1)
    
    ficha=random.randint(1,2)
    if ficha == 1:
        piece='O'
        pcPiece='X'
    else:
        piece='X'
        pcPiece='O'
    mb.showinfo("Tu ficha...", piece)
    # piece = tk.Entry(root)

    num=random.randint(1,2)
    if num==1: #'user'
        mb.showinfo("Info","- Empezas vos...")
    else: # pc
        mb.showinfo("Info","- Empieza la PC...")
        crussesPC()
    root.mainloop()
