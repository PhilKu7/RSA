from math import fmod, sqrt, gcd
import math
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
root = tk.Tk()
root.title("RSA Verschlüsselung")
root.geometry("".join([str(root_width), "x", str(root_height)]))

letters_sepperately = True

label_text_to_number_encrypt = [1]
timeTriggerGGT = 10000000


menu = tk.Menu(root)
root.config(menu=menu)


def not_yet_programmed():
    messagebox.showerror("Verschlüsselungs editor",
                         "Ist noch nicht programmiert!")


# firstMenu = Menu(menu)
# menu.add_cascade(label="Verschlüsselungen", menu=firstMenu)
# firstMenu.add_command(label="Cäsar-Verschlüsselung",
#                       command=not_yet_programmed)
# firstMenu.add_command(label="Cäsar mit Schlüsselwort Verschlüsselung",
#                       command=not_yet_programmed)
# firstMenu.add_command(label="Polyalphabetische-Verschlüsselung",
#                       command=not_yet_programmed)
# firstMenu.add_command(label="Vignière-Verschlüsselung",
#                       command=not_yet_programmed)
# firstMenu.add_separator()
# firstMenu.add_command(label="Skytale", command=not_yet_programmed)

zentrierDivisor = 100000


def check_prime(number, is_random_prime, count=1):
    n = None
    if is_random_prime == True:
        if number <= 1:
            n = input_prime(is_random_prime)
        else:
            for i in range(2, int(sqrt(number))+1):
                if number*1.0 % i == 0:
                    n = input_prime(is_random_prime)
                    break
    else:
        if number <= 1:
            error = f"Error 1: The number you entered ({number}) was not a prime."
            messagebox.showerror(
                "RSA", f"The following error occured:\n{error} \n\nplease try again")
            n = input_prime(is_random_prime, count)
        else:
            for i in range(2, int(sqrt(number))+1):
                if number*1.0 % i == 0:
                    error = f"Error 1: The number you entered ({number}) was not a prime."
                    messagebox.showerror(
                        "RSA", f"The following error occured:\n{error} \n\nplease try again")
                    n = input_prime(is_random_prime, count)
                    break
    if n != None:
        return n
    else:
        return number


def input_prime(is_random_prime, count=1):
    if is_random_prime == True:
        n = random.randint(h, g)
        n = check_prime(n, is_random_prime)
    else:
        if count == 1:
            n = check_prime(Dialogs.input_Int(root, "Enter prime",
                                              "What is your first prime number? (p)", "11"), False, count)
        elif count == 2:
            n = check_prime(Dialogs.input_Int(root, "Enter prime",
                                              "What is your second prime number? (q)", "17"), False, count)
    return n


def waiting():
    messagebox.showerror("Verschlüsselungs editor",
                         "Immer noch am berechnen!")


def check_error(e, phi_n, d):
    if not (0 <= e <= N-1):
        return f"Error 1: e does not satisfy the following:\n0 <= e <= N-1, where N = {N}"
    if not (math.gcd(e, phi_n) == 1):
        return f"Error 1: e does not satisfy the following:\ngcd(e, 𝜑(n)) = 1, where 𝜑(n) = {phi_n}"
    if not (0 <= d <= N-1):
        return f"Error 1: d does not satisfy the following:\n0 <= d <= N-1, where N = {N}"
    if not ((e*d) % phi_n == 1):
        return f"Error 1: e does not satisfy the following:\ne ∙ d ≡ mod(𝜑(n)), where 𝜑(n) = {phi_n} and d = {d}"
    return False


def prime_factors(n):
    return_list = []
    while n % 2 == 0:
        return_list.append(n)
        n = n / 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            return_list.append(n)
            n = n / i
    if n > 2:
        return_list.append(n)
    return return_list


def define_key_auto():
    global e
    global N
    global phi_n
    global h
    global g
    global d
    global factored_d
    global factored_e
    h = Dialogs.input_Int(
        root, "RSA", "What is your lower bound for your random numbers?", "10")
    g = Dialogs.input_Int(
        root, "RSA", "What is your upper bound for your random numbers?", "100")
    p = input_prime(True)
    q = input_prime(True)
    while p == q:
        p = input_prime(True)
    print(f"p = {p}, q = {q}")
    N = p*q
    phi_n = (p-1)*(q-1)
    e = 1
    while e < N:
        # e = random.randint(2, phi_n-1)
        e += 1
        d = 1
        while not ((e*d) % phi_n == 1) and d < N:
            d += 1
        error = check_error(e, phi_n, d)
        if not error:
            break
    factored_d = prime_factors(d)
    factored_e = prime_factors(e)
    string_e_N = tk.Label(root, text=f"e = {e}\nN = {N}")
    string_e_N.place(x=250, y=60, width=150, height=80)

    string_d = tk.Label(root, text=f"d = {d}")
    string_d.place(x=150, y=250, width=150, height=50)


def define_key():
    global e
    global N
    global phi_n
    global d
    global factored_d
    global factored_e
    d = 0
    p = input_prime(False, 1)
    q = input_prime(False, 2)
    while p == q:
        error = "Error 1: q does not satisfy the following:\np ≠ q"
        messagebox.showerror(
            "RSA", f"The following error occured:\n{error} \n\nplease try again")
        q = input_prime(False, 2)
    N = p*q
    phi_n = (p-1)*(q-1)
    while True:
        e = Dialogs.input_Int(root, "Encipher number",
                              "What is your encipher number? (e)", "7")
        if 0 <= e <= N-1:
            d = 1
            while not (e*d) % phi_n == 1:
                d += 1
        error = check_error(e, phi_n, d)
        if error:
            messagebox.showerror(
                "RSA", f"The following error occured:\n{error} \n\nplease try again")
        else:
            break

    factored_d = prime_factors(d)
    factored_e = prime_factors(e)
    string_e_N = tk.Label(root, text=f"e = {e}\nN = {N}")
    string_e_N.place(x=250, y=60, width=150, height=80)

    string_d = tk.Label(root, text=f"d = {d}")
    string_d.place(x=150, y=250, width=150, height=50)


def encrypt():
    message_string = Dialogs.input_Str(
        root, "Encryption", "What do you want to encrypt?", "Hello World!")
    message = []
    for n in message_string:
        message.append(ord(n))
    print(f"Message = {message}")
    if letters_sepperately == True:
        C = []
        for n in message:
            encrypted_char = n
            # for m in factored_e:
            #     encrypted_char = encrypted_char**m % N
            # n_bin = bin(n)[3:]
            # print(f"{n_bin}, {n_bin[::-1]}")
            e_bin = format(e, "b")
            print(e_bin)
            # for m in n_bin:
            #     if m==0:
            #         del n_bin[m]
            #     else:
            #         break
            for m in e_bin[1:]:
                # print(m, end="")
                encrypted_char = encrypted_char**2 % N
                if int(m) == 1:
                    encrypted_char = encrypted_char*n % N
            # print(bin(n))
            # print(bin(n)[::-1])

            C.append(encrypted_char)
    Dialogs.input_Str(root, "Encryption",
                      "Your encrypted message:", C)


def decrypt():
    C = Dialogs.input_Str(root, "Encryption",
                          "What do you want to decrypt?", "")
    C_list = []
    first = 0
    for n in range(len(C)):
        if C[n] == " ":
            C_list.append(C[first:n])
            first = n+1
    C_list.append(C[first:])
    print(f"C = {C_list}")
    message = []
    for n in C_list:
        # decrypted_char = int(n)
        # for m in factored_d:
        #     decrypted_char = decrypted_char**m % N
        decrypted_char = int(n)
        d_bin = format(d, "b")
        for m in  d_bin[1:]:
            decrypted_char = decrypted_char**2 % N
            if int(m) == 1:
                decrypted_char = decrypted_char*int(n) % N

        message.append(chr(decrypted_char))
        print(f"decrypt({n}) = {decrypted_char} = {message[-1]}")
    end_message = ""
    for n in range(len(message)):
        end_message = end_message + message[n]
    Dialogs.input_Str(root, "Encryption",
                      "Your decrypted message:", end_message)


button_define_key = tk.Button(root, text=label_define_key[4], command=define_key,
                              background="#FFFF00", activebackground="#FFF000",  cursor="exchange", borderwidth=5)
button_define_key.place(x=root_x_start+root_borderwidth,
                        y=root_height-root_borderwidth -
                        label_define_key[2],
                        width=label_define_key[3], height=label_define_key[2])

button_define_key_auto = tk.Button(root, text=label_define_key_auto[4], command=define_key_auto,
                                   background="#FFFF00", activebackground="#FFF000", cursor="exchange", borderwidth=5)
button_define_key_auto.place(x=root_width-root_borderwidth-label_define_key_auto[3],
                             y=root_height-root_borderwidth -
                             label_define_key_auto[2],
                             width=label_define_key_auto[3], height=label_define_key_auto[2])

button_encrypt = tk.Button(root, text=label_encrypt_text[4], command=encrypt,
                           background="#7CFC00", activebackground="#80FF07",  cursor="exchange", borderwidth=5)
button_encrypt.place(
    x=root_width/2-label_encrypt_text[3]/2, y=label_encrypt_text[1], width=label_encrypt_text[3], height=label_encrypt_text[2])

button_decrypt = tk.Button(root, text=label_decrypt_text[4], command=decrypt,
                           background="#40E0D0", activebackground="#48D1CC", cursor="exchange", borderwidth=5)
button_decrypt.place(
    x=root_width/2-label_decrypt_text[3]/2, y=label_decrypt_text[1], width=label_decrypt_text[3], height=label_decrypt_text[2])


if __name__ == "__main__":
    root.mainloop()
