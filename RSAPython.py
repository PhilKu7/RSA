##from gpanel import *
##from thread import start_new_thread
from math import fmod,sqrt
import random
from Dialogs import*
from tkinter import *
from tkinter import simpledialog,messagebox
window_x_start = 0
window_y_start = 0
window_width = 750
window_height = 500
window_borderwidth = 10
b = [str(window_width), 'x', str(window_height)]
a = ''.join(b)
window = Tk()
window.title('RSA Verschlüsselung')
window.geometry(a)

print(input_Int("hallo", "Drücke OK", "Schreibe etwas"))

feldSchluesselSelbstDefinieren = [0, 0, 50, 200,'Schlüssel selbst definieren',
                                  'yellow']             #(x, y, height, width)
feldSchluesselAutomatischDefinieren = [300, 0, 50, 200,
                                       'Schlüssel automatisch definieren',
                                       'yellow']        #(x, y, height, width)
feldTextInZahlVerschluesseln = [1]
timeTriggerGGT = 10000000


menu = Menu(window)
window.config(menu=menu)

def nochNichtProgrammiert():
    messagebox.showerror('Verschlüsselungs editor',
                         'Ist noch nicht programmiert!')

firstMenu = Menu(menu)
menu.add_cascade(label='Verschlüsselungen',menu=firstMenu)
firstMenu.add_command(label='Cäsar-Verschlüsselung',
                      command = nochNichtProgrammiert)
firstMenu.add_command(label='Cäsar mit Schlüsselwort Verschlüsselung',
                      command = nochNichtProgrammiert)
firstMenu.add_command(label='Polyalphabetische-Verschlüsselung',
                      command = nochNichtProgrammiert)
firstMenu.add_command(label='Vignière-Verschlüsselung',
                      command = nochNichtProgrammiert)
firstMenu.add_separator()
firstMenu.add_command(label='Skytale', command = nochNichtProgrammiert)

zentrierDivisor = 100000

def stringEN():
    setColor('BLACK')
    text(250, 100,str(e))
    text(250, 120,str(N))

def primzahlPruefenP(zahl):
    pruefung = 0
    if zahl <= 1:
        msgDlg("Die von dir eingegebene Zahl",zahl,
               "ist keine Primzahl.\nBitte eine ander eingeben.")
        eingabeP()
    for i in range (2,int(sqrt(zahl))+1):
        if zahl*1.0%i == 0:
            pruefung = 1
    if pruefung == 1:
        msgDlg("Die von dir eingegebene Zahl",zahl,
               "ist keine Primzahl.\nBitte eine ander eingeben.")
        eingabeP()

def primzahlPruefenQ(zahl):
    pruefung = 0
    if zahl <= 1:
        msgDlg("Die von dir eingegebene Zahl",zahl,
               "ist keine Primzahl.\nBitte eine ander eingeben.")
        eingabeQ()
    for i in range (2,int(sqrt(zahl))+1):
        if zahl*1.0%i == 0:
            pruefung = 1
    if pruefung == 1:
        msgDlg("Die von dir eingegebene Zahl",zahl,
               "ist keine Primzahl.\nBitte eine ander eingeben.")
        eingabeQ()

def primzahlPruefenP1(zahl):
    pruefung = 0
    if zahl <= 1:
        eingabeP1()
    for i in range (2,int(sqrt(zahl))+1):
        if zahl*1.0%i == 0:
            pruefung = 1
    if pruefung == 1:
        eingabeP1()

def primzahlPruefenQ1(zahl):
    pruefung = 0
    if zahl <= 1:
        eingabeQ1()
    for i in range (2,int(sqrt(zahl))+1):
        if zahl*1.0%i == 0:
            pruefung = 1
    if pruefung == 1:
        eingabeQ1()

def eingabeP():
    global p
    p = simpledialog.askinteger('Primzahl eintippen',
                                'Was ist deine erste Primzahl? (p)',
                                initialvalue=11)
    primzahlPruefenP(p)

def eingabeQ():
    global q
    q = simpledialog.askinteger('Primzahl eintippen',
                                'Was ist deine zweite Primzahl? (q)',
                                initialvalue=5)
    primzahlPruefenQ(q)

def eingabeP1():
    global p
    p = random.randint(h,g)
    primzahlPruefenP1(p)
    
def eingabeQ1():
    global q
    q = random.randint(h,g)
    primzahlPruefenQ1(q)
    
def schluesselDefinierenAutomatisch():
    global e
    global N
    global a
    global h
    global g
    global d
    h = input_Int('RSA','Was ist die tiefste Zufallszahl?',10)
    g = input_Int('RSA','Was ist die höchste Zufallszahl?',100)
    eingabeP1()   # Eingabe von p
    eingabeQ1()   # Eingabe von Q
    while p == q:
        eingabeP1()
    N = p*q
    a = (p-1)*(q-1)
    e = random.randint(h,g)
    bb = e              # ggT herausfinden
    aa = a
    time = 0
    while bb != 0 and time < timeTriggerGGT:
        time = time+1
        rest = aa%bb
        aa = bb
        bb = rest
    while 1 > e or e >= N or aa != 1:                # Zahl 'e' prüfen
        if aa != 1:
            e = random.randint(h,g)
            bb = e              # ggT herausfinden
            aa = a
            time = 0
            while not bb == 0 and time < timeTriggerGGT:
                time = time+1
                rest = aa%bb
                aa = bb
                bb = rest
        if 1 > e:
            e = random.randint(h,g)
        if e >= N:
            e = random.randint(h,g)
##    setColor('WHITE')
    fillRectangle(feldTextVerschluesseln[0],feldTextVerschluesseln[1],
                  feldTextVerschluesseln[2],feldTextVerschluesseln[3])
##    setColor('BLACK')
    text((feldTextVerschluesseln[2]-feldTextVerschluesseln[0])/2
         +feldTextVerschluesseln[0]-len('ein kleiner Moment Geduld')
         /zentrierDivisor,
    (feldTextVerschluesseln[3]-feldTextVerschluesseln[1])/2
         +feldTextVerschluesseln[1]-5,'ein kleiner Moment Geduld')
##    setColor('WHITE')
    fillRectangle(250, 60, 400, 140)
    stringEN()
#    msgDlg('Dein öffentlicher Schlüssel ist:\nN =',N,'\ne =',e)
    d = 1
    while not (e*d)%a == 1:
        d = d+1
##    setColor('LIGHTGREEN')
    fillRectangle(150, 250, 350, 350)
##    setColor('BLACK')
    text((feldTextVerschluesseln[2]-feldTextVerschluesseln[0])/2
         +feldTextVerschluesseln[0]-len(feldTextVerschluesseln[4])
         /zentrierDivisor,
    (feldTextVerschluesseln[3]-feldTextVerschluesseln[1])/2
         +feldTextVerschluesseln[1]-5,feldTextVerschluesseln[4])
#    msgDlg('Dein privater Schlüssel ist:\nd =',d)
##    setColor('BLACK')
    text(250, 60,str(d))
    
def schluesselDefinieren():
    global e
    global N
    global a
    global d
    eingabeP()   # Eingabe von p
    eingabeQ()   # Eingabe von Q
    while p == q:
        msgDlg('Du darfst keine gleichen Zahlen auswählen.\nBitte gib neue Zahlen ein.')
        eingabeP()
    N = p*q
    a = (p-1)*(q-1)
    e = simpledialog.askinteger('Encipher Zahl','Was ist deine "encipher" Zahl? (e)',initialvalue=27)
    bb = e              # ggT herausfinden
    aa = a
    time = 0
    while not bb == 0 and time < timeTriggerGGT:
        time = time+1
        rest = aa%bb
        aa = bb
        bb = rest
#        print('rest:',rest)
    while 1 > e or e >= N or aa != 1:                # Zahl 'e' prüfen
        if aa != 1:
#            msgDlg('')
            e = inputInt('Du darfst keine Zahle, die den ggt von ihr und "p*q" , 1 gibt gebrauchen.\nBitte gib eine neue Zahle für "e" ein.\nWas ist deine "encipher" Zahl? (e)')
            bb = e              # ggT herausfinden
            aa = a
            time = 0
            while not bb == 0 and time < timeTriggerGGT:
                time = time+1
                rest = aa%bb
                aa = bb
                bb = rest
#                print('rest:',rest)
        if 1 > e:
#            msgDlg('')
            e = inputInt('Du darfst keine Zahle kleiner als 1 auswählen.\nBitte gib eine neue Zahle für "e" ein.\nWas ist deine "encipher" Zahl? (e)')
        if e >= N:
#            msgDlg('')
            e = inputInt('Du darfst keine Zahle grösser als "p*q" auswählen.\nBitte gib eine neue Zahle für "e" ein.\nWas ist deine "encipher" Zahl? (e)')
##    setColor('WHITE')
    fillRectangle(feldTextVerschluesseln[0],feldTextVerschluesseln[1],feldTextVerschluesseln[2],feldTextVerschluesseln[3])
##    setColor('BLACK')
    text((feldTextVerschluesseln[2]-feldTextVerschluesseln[0])/2+feldTextVerschluesseln[0]-len('ein kleiner Moment Geduld')/zentrierDivisor,
    (feldTextVerschluesseln[3]-feldTextVerschluesseln[1])/2+feldTextVerschluesseln[1]-5,'ein kleiner Moment Geduld')
##    setColor('WHITE')
    fillRectangle(250, 60, 400, 140)
    stringEN()
#    msgDlg('Dein öffentlicher Schlüssel ist:\nN =',N,'\ne =',e)
    d = 1
    while not (e*d)%a == 1:
        d = d+1
##    setColor('LIGHTGREEN')
    fillRectangle(150, 250, 350, 350)
##    setColor('BLACK')
    text((feldTextVerschluesseln[2]-feldTextVerschluesseln[0])/2+feldTextVerschluesseln[0]-len(feldTextVerschluesseln[4])/zentrierDivisor,
    (feldTextVerschluesseln[3]-feldTextVerschluesseln[1])/2+feldTextVerschluesseln[1]-5,feldTextVerschluesseln[4])
#    msgDlg('Dein privater Schlüssel ist:\nd =',d)
##    setColor('BLACK')
    text(250, 60,str(d))

def verschluesseln():
    mString = inputString('Was wollen sie verschlüsseln?\nNur ein Buchstabe.')
    m = ord(mString)
    c = m^e%N
    msgDlg('Ihr verschlüsselter Text lautet:\n',c) 
    
def entschluesseln():
    subtract = '0x'
    cInt = inputInt('Was wollen sie entschlüsseln?')
    m = cInt^d%N
    mInt = hex(m)
##    mEnd = mInt.replace('0x','\x')
##    uni = R'\'
    End = uni+mEnd
    msgDlg(End)
    msgDlg('Ihr Text lautet:\n',End)

feldTextVerschluesseln = [312, 200, 30, 124,'Text verschlüsseln','lightgreen']                                     #(x, y, height, width)
feldTextEntschluesseln = [312, 300, 30, 124,'Text entschlüsseln','lightblue' ]                                     #(x, y, height, width)



schluesselDefinierenKnopf = Button(window, text=feldSchluesselSelbstDefinieren[4], command=schluesselDefinieren,
                                   background='#FFFF00', activebackground='#FFF000',  cursor='exchange', borderwidth=5)
schluesselDefinierenKnopf.place(x = window_x_start+window_borderwidth,
                                y=window_height-window_borderwidth-feldSchluesselSelbstDefinieren[2],
                                width=feldSchluesselSelbstDefinieren[3], height=feldSchluesselSelbstDefinieren[2])

schluesselDefinierenAutomatischKnopf = Button(window, text=feldSchluesselAutomatischDefinieren[4], command=schluesselDefinierenAutomatisch,
                                              background='#FFFF00', activebackground='#FFF000', cursor='exchange', borderwidth=5)
schluesselDefinierenAutomatischKnopf.place(x = window_width-window_borderwidth-feldSchluesselAutomatischDefinieren[3],
                                           y=window_height-window_borderwidth-feldSchluesselAutomatischDefinieren[2],
                                           width=feldSchluesselAutomatischDefinieren[3], height=feldSchluesselAutomatischDefinieren[2])

verschluesselnKnopf = Button(window, text=feldTextVerschluesseln[4], command=verschluesseln,
                             background='#7CFC00', activebackground='#80FF07',  cursor='exchange', borderwidth=5)
verschluesselnKnopf.place(x=window_width/2-feldTextVerschluesseln[3]/2, y=feldTextVerschluesseln[1], width=feldTextVerschluesseln[3], height=feldTextVerschluesseln[2])

entschluesselnKnopf = Button(window, text=feldTextEntschluesseln[4], command=entschluesseln,
                             background='#40E0D0', activebackground='#48D1CC', cursor='exchange', borderwidth=5)
entschluesselnKnopf.place(x=window_width/2-feldTextEntschluesseln[3]/2, y=feldTextEntschluesseln[1], width=feldTextEntschluesseln[3], height=feldTextEntschluesseln[2])






















##def onMousePressed(x, y):
##    if x > feldSchluesselSelbstDefinieren[0] and y > feldSchluesselSelbstDefinieren[1] and x < feldSchluesselSelbstDefinieren[2] and y < feldSchluesselSelbstDefinieren[3]:
##        schluesselDefinieren()
##        
##    if x > feldSchluesselAutomatischDefinieren[0] and y > feldSchluesselAutomatischDefinieren[1] and x < feldSchluesselAutomatischDefinieren[2] and y < feldSchluesselAutomatischDefinieren[3]:
##        schluesselDefinierenAutomatisch()
##        
##    if x > 427 and y > 480:
##        dispose()
##        
##    if x > feldTextVerschluesseln[0] and y > feldTextVerschluesseln[1] and x < feldTextVerschluesseln[2] and y < feldTextVerschluesseln[3]:
##        verschluesseln()
##        
##    if x > feldTextEntschluesseln[0] and y > feldTextEntschluesseln[1] and x < feldTextEntschluesseln[2] and y < feldTextEntschluesseln[3]:
##        entschluesseln()
##
##
###def onKeyPressed():
###    dispose()
##
##
####makeGPanel(0, 500, 0, 500, mousePressed = onMousePressed)
####makeGPanel(Size(500, 500))
####windowPosition(700,250)
####window(0, 500, 0, 500)
####image('sprites/exitbtn_0.gif', 472, 480)
####setColor('YELLOW')
##canvas.create_rectangle(feldSchluesselSelbstDefinieren[0],feldSchluesselSelbstDefinieren[1],feldSchluesselSelbstDefinieren[2],feldSchluesselSelbstDefinieren[3],fill=feldSchluesselSelbstDefinieren[5])
##canvas.create_rectangle(feldSchluesselAutomatischDefinieren[0],feldSchluesselAutomatischDefinieren[1],feldSchluesselAutomatischDefinieren[2],feldSchluesselAutomatischDefinieren[3],fill=feldSchluesselAutomatischDefinieren[5])
####setColor('LIGHTGREEN')                                                  #feldTextVerschluesseln
##canvas.create_rectangle(feldTextVerschluesseln[0],feldTextVerschluesseln[1],feldTextVerschluesseln[2],feldTextVerschluesseln[3],fill=feldTextVerschluesseln[5])
####setColor('LIGHTBLUE')                                                   #feldTextEntschluesseln
##canvas.create_rectangle(feldTextEntschluesseln[0],feldTextEntschluesseln[1],feldTextEntschluesseln[2],feldTextEntschluesseln[3],fill=feldTextEntschluesseln[5])
####setColor('BLACK')
##canvas.create_text((feldSchluesselSelbstDefinieren[2]-feldSchluesselSelbstDefinieren[0])/2+feldSchluesselSelbstDefinieren[0]-len(feldSchluesselSelbstDefinieren[4])/zentrierDivisor,
##(feldSchluesselSelbstDefinieren[3]-feldSchluesselSelbstDefinieren[1])/2+feldSchluesselSelbstDefinieren[1]-5,text=feldSchluesselSelbstDefinieren[4]) #21,20
###text(310, 20,'Schlüssel automatisch definieren') 
##canvas.create_text((feldSchluesselAutomatischDefinieren[2]-feldSchluesselAutomatischDefinieren[0])/2+feldSchluesselAutomatischDefinieren[0]-len(feldSchluesselAutomatischDefinieren[4])/zentrierDivisor,
##(feldSchluesselAutomatischDefinieren[3]-feldSchluesselAutomatischDefinieren[1])/2+feldSchluesselAutomatischDefinieren[1]-5,text=feldSchluesselAutomatischDefinieren[4]) 
###text(195, 300,'Text verschlüsseln')
##canvas.create_text((feldTextVerschluesseln[2]-feldTextVerschluesseln[0])/2+feldTextVerschluesseln[0]-len(feldTextVerschluesseln[4])/zentrierDivisor,
##(feldTextVerschluesseln[3]-feldTextVerschluesseln[1])/2+feldTextVerschluesseln[1]-5,text=feldTextVerschluesseln[4])
###text(195, 200,'Text entschlüsseln')
##canvas.create_text((feldTextEntschluesseln[2]-feldTextEntschluesseln[0])/2+feldTextEntschluesseln[0]-len(feldTextEntschluesseln[4])/zentrierDivisor,
##(feldTextEntschluesseln[3]-feldTextEntschluesseln[1])/2+feldTextEntschluesseln[1]-5,text=feldTextEntschluesseln[4])
##
##canvas.create_text(140, 80,text='Privater Schlüssel:')
##canvas.create_text(220, 60,text='d =')
##canvas.create_text(140, 140,text='Öffentlicher Schlüssel:') 
##canvas.create_text(220, 120,text='N =')
##canvas.create_text(220, 100,text='e =')
###start_new_thread(closeWindow, ( ))

