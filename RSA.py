from math import sqrt, gcd
import math
import random
from tkinter import font
import Dialogs
import tkinter as tk
from tkinter import simpledialog, messagebox, Menu
from styles import *

root_x_start = 0
root_y_start = 0
root_borderwidth = 10
root = tk.Tk()
root.title("RSA Encryption")

letters_sepperately = True

label_text_to_number_encrypt = [1]
timeTriggerGGT = 10000000

input_number_of_chars = tk.IntVar()
input_number_of_chars.set(1)

input_encoding_method = tk.StringVar()
input_encoding_method.set("UNICODE")

menu = tk.Menu(root)
root.config(menu=menu)


def raise_error(error):
    messagebox.showerror(
        error_titles, f"The following error occured:\n{error} \n\nplease try again")


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
            raise_error(error)
            n = input_prime(is_random_prime, count)
        else:
            for i in range(2, int(sqrt(number))+1):
                if number*1.0 % i == 0:
                    error = f"Error 1: The number you entered ({number}) was not a prime."
                    raise_error(error)
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
            n = check_prime(Dialogs.input_Int(
                root, "Enter prime", "What is your first prime number? (p)", "11"), False, count)
        elif count == 2:
            n = check_prime(Dialogs.input_Int(
                root, "Enter prime", "What is your second prime number? (q)", "17"), False, count)
    return n


def check_error(e, phi_n, d, N):
    if not (0 <= e <= N-1):
        return f"Error 1: e does not satisfy the following:\n0 <= e <= N-1, where N = {N}"
    if not (math.gcd(e, phi_n) == 1):
        return f"Error 1: e does not satisfy the following:\ngcd(e, 𝜑(n)) = 1, where 𝜑(n) = {phi_n}"
    if not (0 <= d <= N-1):
        return f"Error 1: d does not satisfy the following:\n0 <= d <= N-1, where N = {N}"
    if not (e*d % phi_n == 1):
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


def extended_gcd(a, b):
    u, v, s, t = 1, 0, 0, 1
    while b != 0:
        q = a//b
        a, b, = b, a-q*b
        u, s = s, u-q*s
        v, t = t, v-q*t
    return a, u, v


def define_key_auto():
    global N
    global phi_n
    global d
    global e
    global h
    global g
    h = Dialogs.input_Int(root, "Enter lower bound",
                          "What is your lower bound for your random numbers?", "10")
    g = Dialogs.input_Int(root, "Enter upper bound",
                          "What is your upper bound for your random numbers?", "100")
    while h >= g:
        raise_error(
            f"Error 1: your first number ({h}) is bigger than your second number ({g})")
        h = Dialogs.input_Int(
            root, "RSA", "What is your lower bound for your random numbers?", "10")
        g = Dialogs.input_Int(
            root, "RSA", "What is your upper bound for your random numbers?", "100")
    p = input_prime(True)
    q = input_prime(True)
    while p == q:
        p = input_prime(True)
    local_N = p*q
    local_phi_n = (p-1)*(q-1)
    print(f"p = {p}, q = {q}, 𝜑(n) = {local_phi_n}")
    local_e = random.randint(1, local_phi_n/2)
    while local_e < local_phi_n:
        local_e += 1
        if (gcd(local_e, local_phi_n) != 1):
            continue
        g, u, v = extended_gcd(local_e, local_phi_n)
        local_d = u % local_phi_n
        error = check_error(local_e, local_phi_n, local_d, local_N)
        if not error:
            break
    N, phi_n, d, e = local_N, local_phi_n, local_d, local_e
    print(f"e = {e}, d = {d}, N = {N}")
    string_e_N = tk.Label(root, text=f"e = {e}\nN = {N}")
    string_e_N.grid(column=0, row=2)

    string_d = tk.Label(root, text=f"d = {d}")
    string_d.grid(column=1, row=2)


def define_key():
    global N
    global phi_n
    global d
    global e
    p = input_prime(False, 1)
    q = input_prime(False, 2)
    while p == q:
        error = "Error 1: q does not satisfy the following:\np ≠ q"
        raise_error(error)
        q = input_prime(False, 2)
    local_N = p*q
    local_phi_n = (p-1)*(q-1)
    print(f"p = {p}, q = {q}, 𝜑(n) = {local_phi_n}")
    local_e = random.randint(1, local_phi_n/2)
    while local_e < local_phi_n:
        local_e += 1
        if (gcd(local_e, local_phi_n) != 1):
            continue
        local_e = Dialogs.input_Int(
            root, "Encipher number", "What is your encipher number? (e)", local_e)
        g, u, v = extended_gcd(local_e, local_phi_n)
        local_d = u % local_phi_n
        error = check_error(local_e, local_phi_n, local_d, local_N)
        if not error:
            break
        else:
            raise_error(error)
    N, phi_n, d, e = local_N, local_phi_n, local_d, local_e
    print(f"e = {e}, d = {d}, N = {N}")
    string_e_N = tk.Label(root, text=f"e = {e}\nN = {N}")
    string_e_N.grid(column=0, row=2)

    string_d = tk.Label(root, text=f"d = {d}")
    string_d.grid(column=1, row=2)


def encrypt():
    message_string = Dialogs.input_Str(
        root, "Encryption", "What do you want to encrypt?", "Hello World!")
    while message_string == "":
        raise_error("Error 1: your message to encrypt is empty")
        message_string = Dialogs.input_Str(
            root, "Encryption", "What do you want to encrypt?", "Hello World!")
    message = []
    if input_encoding_method.get() == "UNICODE":
        for n in message_string:
            if ord(n) > N:
                raise_error(
                    f"Error 1: This text \"{message_string}\" contains {input_encoding_method.get()}-symbols bigger than N ({N}) such as \"{n}\" ({ord(n)})!\nThis symbol will be encrypted wrongly!")
            message.append(ord(n))
    elif input_encoding_method.get() == "ASCII":
        for n in message_string:
            if ord(n) > 255:
                raise_error(
                    f"Error 1: This text \"{message_string}\" contains non-ASCII symbols such as \"{n}\"!")
                return
            elif ord(n) > N:
                raise_error(
                    f"Error 1: This text \"{message_string}\" contains {input_encoding_method.get()}-symbols bigger than N ({N}) such as \"{n}\" ({ord(n)})!\nThis symbol will be encrypted wrongly!")
            message.append(ord(n))
    print(f"Message = {message}")
    if input_encoding_method.get() == "ASCII":
        old_message = message
        message = []
        for n in old_message:
            message.append(f"{n:03d}")
        old_message = message
        if len(old_message) % input_number_of_chars.get() != 0:
            for n in range(input_number_of_chars.get()-(len(old_message) % input_number_of_chars.get())):
                old_message.append("000")
        message = []
        part_message = ""
        for n in range(0, len(old_message), input_number_of_chars.get()):
            for m in range(input_number_of_chars.get()):
                part_message += old_message[n+m]
            message.append(part_message)
            part_message = ""
        for n in message:
            if int(n) > N:
                raise_error(
                    f"Error 1: This text \"{message_string}\" contains {input_encoding_method.get()}-symbols bigger than N ({N}) when encrypting {input_number_of_chars.get()} letters at the time!\nE.g. {int(n)} is bigger than N ({N})\nSome symbol will be encrypted wrongly!")
    if letters_sepperately == True:
        C = []
        for n in message:
            encrypted_char = int(n)
            e_bin = format(e, "b")
            print(e_bin)
            for m in e_bin[1:]:
                encrypted_char = encrypted_char**2 % N
                if int(m) == 1:
                    encrypted_char = encrypted_char*int(n) % N
            C.append(encrypted_char)
    Dialogs.input_Str(root, "Encryption", "Your encrypted message:", C)


def decrypt():
    C = Dialogs.input_Str(root, "Encryption",
                          "What do you want to decrypt?", "")
    while C == "":
        raise_error("Error 1: your message to decrypt is empty")
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
        decrypted_char = int(n)
        d_bin = format(d, "b")
        for m in d_bin[1:]:
            decrypted_char = decrypted_char**2 % N
            if int(m) == 1:
                decrypted_char = decrypted_char*int(n) % N
        if input_encoding_method.get() == "ASCII":
            decrypted_char = str(decrypted_char)
            while len(decrypted_char) % input_number_of_chars.get() != 0:
                decrypted_char = "0"+decrypted_char
            segments = int(len(decrypted_char)/input_number_of_chars.get())
            for m in range(input_number_of_chars.get()):
                message.append(chr(
                    int(decrypted_char[m*segments:(m+1)*segments])))
                print(
                    f"decrypt({n}) = {decrypted_char}; schar({decrypted_char[m*segments:(m+1)*segments]}) = {message[-1]}")
        else:
            message.append(chr(decrypted_char))
            print(f"decrypt({n}) = {decrypted_char} = {message[-1]}")
    end_message = ""
    for n in range(len(message)):
        end_message = end_message + message[n]
    Dialogs.input_Str(root, "Encryption",
                      "Your decrypted message:", end_message)


# ----------- style labels -----------
label_title_RSA = {"text": "RSA Encryption", "font": font.BOLD}
label_button_encrypt = {"text": "Encrypt text", "command": encrypt, "background": "#7CFC00",
                        "activebackground": "#80FF07",  "cursor": "exchange", "borderwidth": 5}
label_button_decrypt = {"text": "Decrypt text", "command": decrypt, "background": "#40E0D0",
                        "activebackground": "#48D1CC", "cursor": "exchange", "borderwidth": 5}
label_button_define_key = {"text": "Define key manually", "command": define_key,
                           "background": "#FFFF00", "activebackground": "#FFF000",  "cursor": "pencil", "borderwidth": 5}
label_button_define_key_auto = {"text": "Define key automatic", "command": define_key_auto,
                                "background": "#FFFF00", "activebackground": "#FFF000", "cursor": "pencil", "borderwidth": 5}
label_input_number_of_chars_1 = {
    "text": "only 1 letter", "variable": input_number_of_chars, "value": 1}
label_input_number_of_chars_2 = {
    "text": "every 2 letters", "variable": input_number_of_chars, "value": 2}
label_input_encoding_method_ASCII = {
    "text": "ASCII", "variable": input_encoding_method, "value": "ASCII"}
label_input_encoding_method_UNICODE = {
    "text": "UNICODE", "variable": input_encoding_method, "value": "UNICODE"}

label_input_number_of_chars = {
    "text": "only 1 letter", "textvariable": input_number_of_chars,  "from_": 1, "to": 10, "increment": 1}

# ----------- create and place buttons -----------
tk.Label(root, **label_title_RSA).grid(
    column=0, row=0, columnspan=3)

button_define_key = tk.Button(root, **label_button_define_key)
button_define_key.grid(column=0, row=1, sticky=tk.N+tk.E+tk.S+tk.W)

button_define_key_auto = tk.Button(root, **label_button_define_key_auto)
button_define_key_auto.grid(column=1, row=1, sticky=tk.N+tk.E+tk.S+tk.W)

button_encrypt = tk.Button(root, **label_button_encrypt)
button_encrypt.grid(column=0, row=3, sticky=tk.N+tk.E+tk.S+tk.W)

button_decrypt = tk.Button(root, **label_button_decrypt)
button_decrypt.grid(column=1, row=3, sticky=tk.N+tk.E+tk.S+tk.W)

input_number_of_chars_1 = tk.Radiobutton(root, **label_input_number_of_chars_1)
input_number_of_chars_1.grid(column=0, row=4, sticky=tk.W)

input_number_of_chars_2 = tk.Radiobutton(root, **label_input_number_of_chars_2)
input_number_of_chars_2.grid(column=0, row=5, sticky=tk.W)

input_number_of_chars_ = tk.Spinbox(root, **label_input_number_of_chars)
input_number_of_chars_.grid(column=0, row=6, sticky=tk.W)

input_encoding_method_ASCII = tk.Radiobutton(
    root, **label_input_encoding_method_ASCII)
input_encoding_method_ASCII.grid(column=1, row=4, sticky=tk.W)

input_encoding_method_UNICODE = tk.Radiobutton(
    root, **label_input_encoding_method_UNICODE)
input_encoding_method_UNICODE.grid(column=1, row=5, sticky=tk.W)


if __name__ == "__main__":
    root.mainloop()
