from math import fmod, sqrt
import random
import Dialogs
import tkinter as tk
from tkinter import simpledialog, messagebox, Menu
from styles import *

root_x_start = 0
root_y_start = 0
root_width = 750
root_height = 500
root_borderwidth = 10
b = [str(root_width), 'x', str(root_height)]
a = ''.join(b)
root = tk.Tk()
root.title('RSA Verschlüsselung')
root.geometry(a)

letters_sepperately = True

feldSchluesselSelbstDefinieren = [0, 0, 50, 200, 'Schlüssel selbst definieren',
                                  'yellow']  # (x, y, height, width)
feldSchluesselAutomatischDefinieren = [300, 0, 50, 200,
                                       'Schlüssel automatisch definieren',
                                       'yellow']  # (x, y, height, width)
feldTextInZahlVerschluesseln = [1]
timeTriggerGGT = 10000000


menu = tk.Menu(root)
root.config(menu=menu)


def nochNichtProgrammiert():
    messagebox.showerror('Verschlüsselungs editor',
                         'Ist noch nicht programmiert!')


firstMenu = Menu(menu)
menu.add_cascade(label='Verschlüsselungen', menu=firstMenu)
firstMenu.add_command(label='Cäsar-Verschlüsselung',
                      command=nochNichtProgrammiert)
firstMenu.add_command(label='Cäsar mit Schlüsselwort Verschlüsselung',
                      command=nochNichtProgrammiert)
firstMenu.add_command(label='Polyalphabetische-Verschlüsselung',
                      command=nochNichtProgrammiert)
firstMenu.add_command(label='Vignière-Verschlüsselung',
                      command=nochNichtProgrammiert)
firstMenu.add_separator()
firstMenu.add_command(label='Skytale', command=nochNichtProgrammiert)

zentrierDivisor = 100000


def check_prime(zahl, random_prime, anzahl=1):
    n = None
    if random_prime == True:
        if zahl <= 1:
            n = input_prime(random_prime)
        else:
            for i in range(2, int(sqrt(zahl))+1):
                if zahl*1.0 % i == 0:
                    n = input_prime(random_prime)
                    break
    else:
        if zahl <= 1:
            message = ["Die von dir eingegebene Zahl ", str(
                zahl), " ist keine Primzahl.\nBitte eine ander eingeben."]
            message = "".join(message)
            messagebox.showerror("Verschluesselungserror", message)
            n = input_prime(random_prime, anzahl)
        else:
            for i in range(2, int(sqrt(zahl))+1):
                if zahl*1.0 % i == 0:
                    message = ["Die von dir eingegebene Zahl ", str(
                        zahl), " ist keine Primzahl.\nBitte eine ander eingeben."]
                    message = "".join(message)
                    messagebox.showerror("Verschluesselungserror", message)
                    n = input_prime(random_prime, anzahl)
                    break
    if n != None:
        return n
    else:
        return zahl


def input_prime(random_prime, anzahl=1):
    if random_prime == True:
        n = random.randint(h, g)
        n = check_prime(n, random_prime)
    else:
        if anzahl == 1:
            n = Dialogs.input_Int(root, "Primzahl eintippen",
                                  "Was ist deine erste Primzahl? (p)", "11")
            n = check_prime(n, random_prime, anzahl)
        elif anzahl == 2:
            n = Dialogs.input_Int(root, "Primzahl eintippen",
                                  "Was ist deine zweite Primzahl? (q)", "5")
            n = check_prime(n, random_prime, anzahl)
    return n


def waiting():
    messagebox.showerror('Verschlüsselungs editor',
                         'Immer noch am berechnen!')


def define_key_auto():
    global e
    global N
    global a
    global h
    global g
    global d
    h = Dialogs.input_Int(
        root, 'RSA', 'Was ist die tiefste Zufallszahl?', "10")
    g = Dialogs.input_Int(
        root, 'RSA', 'Was ist die höchste Zufallszahl?', "100")
    p = input_prime(True)  # Eingabe von p
    q = input_prime(True)  # Eingabe von Q
    while p == q:
        p = input_prime(True)  # Eingabe von p
    print("p =", p, "q =", q)
    N = p*q
    a = (p-1)*(q-1)
    e = random.randint(2, a-1)
    bb = e  # ggT herausfinden
    aa = a
    time = 0
    while bb != 0 and time < timeTriggerGGT:
        time = time+1
        rest = aa % bb
        aa = bb
        bb = rest
    while 1 > e or e >= N or aa != 1:  # Zahl 'e' prüfen
        if aa != 1:
            e = random.randint(2, a-1)
            bb = e  # ggT herausfinden
            aa = a
            time = 0
            while not bb == 0 and time < timeTriggerGGT:
                time = time+1
                rest = aa % bb
                aa = bb
                bb = rest
        if 1 > e:
            e = random.randint(2, a-1)
        if e >= N:
            e = random.randint(2, a-1)
    message = ["e = ", str(e), "N = ", str(N)]
    message = "".join(message)
    string_e_N = tk.Label(root, text=message)
    string_e_N.place(x=250, y=60, width=150, height=80)
    print("e =", e, "N =", N)
    d = 1
    while not (e*d) % a == 1:
        d = d+1
    message = ["d = ", str(d)]
    message = "".join(message)
    string_d = tk.Label(root, text=message)
    string_d.place(x=150, y=250, width=200, height=100)
    print("d =", d)


def define_key():
    global e
    global N
    global a
    global d
    p = input_prime(False, 1)  # Eingabe von p
    q = input_prime(False, 2)  # Eingabe von Q
    while p == q:
        messagebox.showerror(
            'RSA', 'Du darfst keine gleichen Zahlen auswählen.\nBitte gib neue Zahlen ein.')
        q = input_prime(False, 2)  # Eingabe von Q
    N = p*q
    a = (p-1)*(q-1)
    e = Dialogs.input_Int(root, 'Encipher Zahl',
                          'Was ist deine "encipher" Zahl? (e)', "27")
    bb = e  # ggT herausfinden
    aa = a
    time = 0
    while not bb == 0 and time < timeTriggerGGT:
        time = time+1
        rest = aa % bb
        aa = bb
        bb = rest
    while 1 > e or e >= N or aa != 1:  # Zahl 'e' prüfen
        if aa != 1:
            message = []
            e = Dialogs.input_Int(
                root, "Encipher Zahl", 'Du darfst keine Zahle, die den ggt von ihr und "p*q" , 1 gibt gebrauchen.\nBitte gib eine neue Zahle für "e" ein.\nWas ist deine "encipher" Zahl? (e)', "")
            bb = e  # ggT herausfinden
            aa = a
            time = 0
            while not bb == 0 and time < timeTriggerGGT:
                time = time+1
                rest = aa % bb
                aa = bb
                bb = rest
        if 1 > e:
            e = Dialogs.input_Int(
                root, "Encipher Zahl", 'Du darfst keine Zahle kleiner als 1 auswählen.\nBitte gib eine neue Zahle für "e" ein.\nWas ist deine "encipher" Zahl? (e)', "")
        if e >= N:
            e = Dialogs.input_Int(
                root, "Encipher Zahl", 'Du darfst keine Zahle grösser als "p*q" auswählen.\nBitte gib eine neue Zahle für "e" ein.\nWas ist deine "encipher" Zahl? (e)', "")
    message = ["e = ", str(e), "N = ", str(N)]
    message = "".join(message)
    string_e_N = tk.Label(root, text=message)
    string_e_N.place(x=250, y=60, width=150, height=80)
    #    msgDlg('Dein öffentlicher Schlüssel ist:\nN =',N,'\ne =',e)
    d = 1
    while not (e*d) % a == 1:
        d = d+1
    message = ["d = ", str(d)]
    message = "".join(message)
    string_d = tk.Label(root, text=message)
    string_d.place(x=150, y=250, width=200, height=100)


def encrypt():
    mString = Dialogs.input_Str(
        root, "Verschlüsselung", 'Was wollen sie verschlüsseln?', "Hallo")
    m = []
    if letters_sepperately == True:
        for n in range(len(mString)):
            m.append(ord(mString[n]))
        # m = ord(mString)
        print("m =", m)
        C = []
        for n in range(len(m)):
            C.append(m[n]**e % N)
        # C = (m**e) % N
    Dialogs.input_Str(root, "Verschlüsselung",
                      "Ihr verschlüsselter Text lautet:", C)


def decrypt():
    C = Dialogs.input_Str(root, "Verschlüsselung",
                          'Was wollen sie entschlüsseln?', "")
    C_list = []
    first = 0
    for n in range(len(C)):
        if C[n] == " ":
            C_list.append(C[first:n])
            first = n
    C_list.append(C[first:])
    print(C_list)
    message = []
    for n in range(len(C_list)):
        letter = int(C_list[n])**d % N
        print("letter", n, "=", letter, chr(letter))
        message.append(chr(letter))
    # m = (C**d) % N
    # print("m = ", message)
    # message = chr(m)
    end_message = ""
    for n in range(len(message)):
        if message[n] != " ":
            end_message = end_message + message[n]
    Dialogs.input_Str(root, "Verschlüsselung",
                      "Ihr entschlüsselter Text lautet:", end_message)


button_define_key = tk.Button(root, text=feldSchluesselSelbstDefinieren[4], command=define_key,
                              background='#FFFF00', activebackground='#FFF000',  cursor='exchange', borderwidth=5)
button_define_key.place(x=root_x_start+root_borderwidth,
                        y=root_height-root_borderwidth -
                        feldSchluesselSelbstDefinieren[2],
                        width=feldSchluesselSelbstDefinieren[3], height=feldSchluesselSelbstDefinieren[2])

button_define_key_auto = tk.Button(root, text=feldSchluesselAutomatischDefinieren[4], command=define_key_auto,
                                   background='#FFFF00', activebackground='#FFF000', cursor='exchange', borderwidth=5)
button_define_key_auto.place(x=root_width-root_borderwidth-feldSchluesselAutomatischDefinieren[3],
                             y=root_height-root_borderwidth -
                             feldSchluesselAutomatischDefinieren[2],
                             width=feldSchluesselAutomatischDefinieren[3], height=feldSchluesselAutomatischDefinieren[2])

button_encrypt = tk.Button(root, text=label_encrypt_text[4], command=encrypt,
                           background='#7CFC00', activebackground='#80FF07',  cursor='exchange', borderwidth=5)
button_encrypt.place(
    x=root_width/2-label_encrypt_text[3]/2, y=label_encrypt_text[1], width=label_encrypt_text[3], height=label_encrypt_text[2])

button_decrypt = tk.Button(root, text=label_decrypt_text[4], command=decrypt,
                           background='#40E0D0', activebackground='#48D1CC', cursor='exchange', borderwidth=5)
button_decrypt.place(
    x=root_width/2-label_decrypt_text[3]/2, y=label_decrypt_text[1], width=label_decrypt_text[3], height=label_decrypt_text[2])


if __name__ == "__main__":
    root.mainloop()
