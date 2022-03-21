import random as random
import os
import tkinter as tk
from tkinter import *
import threading


def begin():
    count = 0
    memory = []
    f = open("fiveletterwords.txt", "r")
    line_num = random.randint(1, 2051)
    for x in range(line_num):
        answer = f.readline()
    attempt_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                    'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                    'y': 0, 'z': 0}
    qwerty = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '\n', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              '\n', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '\n']
    answer_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                   'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                   'y': 0, 'z': 0}

    for x in range(5):
        answer_dict[answer[x]] += 1

    return count, memory, answer, attempt_dict, qwerty, answer_dict


def clear(T):
    T.delete("1.0", "end")


def add(T, text, color):
    if color == "Black":
        T.insert(tk.END, text)
    else:
        T.insert(tk.END, text, color)


def new_game():
    global memory
    global count
    global line_num
    global answer
    global attempt_dict
    global answer_dict
    global qwerty
    clear(T)
    clear(Keyboard)
    count, memory, answer, attempt_dict, qwerty, answer_dict = begin()

    for key in qwerty:
        add(Keyboard, key, "Black")


def wordle():
    global count
    if count == 6:
        return
    correct = 0

    clear(T)
    clear(Keyboard)
    inp = inputtxt.get(1.0, "end-1c")
    inp = inp.lower()
    clear(inputtxt)

    guess_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                  'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                  'y': 0, 'z': 0}

    for x in range(5):
        guess_dict[inp[x]] += 1
    memory.append(["Attempt ({}/6) - ".format(str(count+1)), "Black"])
    temp = answer

    for x in range(5):
        if inp[x] == temp[x]:
            memory.append([inp[x], "Green"])
            temp = temp[:x] + '_' + temp[x + 1:]
            correct += 1
            attempt_dict[inp[x]] = 3
        elif inp[x] in temp and guess_dict[inp[x]] <= answer_dict[inp[x]]:
            memory.append([inp[x], "Red"])
            if attempt_dict[inp[x]] != 3:
                attempt_dict[inp[x]] = 2
        else:
            memory.append([inp[x], "Black"])
            if attempt_dict[inp[x]] != 2 and attempt_dict[inp[x]] != 3:
                attempt_dict[inp[x]] = 1
        if inp[x] in temp:
            guess_dict[inp[x]] -= 1
    memory.append(['\n', "Black"])

    for key in qwerty:
        if key == '\n':
            add(Keyboard, key, "Black")
        elif attempt_dict[key] == 0:
            if key == 'z':
                add(Keyboard, ' ' + key, "Black")
            else:
                add(Keyboard, key, "Black")
        elif attempt_dict[key] == 1:
            if key == 'z':
                add(Keyboard, ' ' + key, "Grey")
            else:
                add(Keyboard, key, "Grey")
        elif attempt_dict[key] == 2:
            if key == 'z':
                add(Keyboard, ' ' + key, "Red")
            else:
                add(Keyboard, key, "Red")
        elif attempt_dict[key] == 3:
            if key == 'z':
                add(Keyboard, ' ' + key, "Green")
            else:
                add(Keyboard, key, "Green")

    if correct == 5:
        memory.append(["You got it, you win!", "Black"])

    if count == 5:
        memory.append(["You ran out of tries, you lose!\n", "Black"])
        memory.append(["The word was: "+answer, "Black"])

    count += 1
    for line in memory:
        add(T, line[0], line[1])


count, memory, answer, attempt_dict, qwerty, answer_dict = begin()

root = tk.Tk()

# specify size of window.
root.geometry("600x400")
T = tk.Text(root, height=15, width=52)
Keyboard = tk.Text(root, height=3, width=10)
# Create label
l = tk.Label(root, text="David's Wordle")
l.config(font=("Courier", 14))


text_box = """"""

l.pack()
T.pack()

# Insert The Fact.
T.insert(tk.END, text_box)
T.tag_config('Red', foreground="red")
T.tag_config('Green', foreground="green")
T.tag_config('Grey', foreground="grey")
Keyboard.tag_config('Red', foreground="red")
Keyboard.tag_config('Green', foreground="green")
Keyboard.tag_config('Grey', foreground="grey")
Keyboard.place(relx=.8, rely=.8, anchor='center')

# TextBox Creation
inputtxt = tk.Text(root,
                   height=5,
                   width=20)
inputtxt.pack()

# Button Creation
printButton = tk.Button(root,
                        text="Try",
                        command=wordle)
printButton.pack()
newButton = tk.Button(root,
                      text="New Game",
                      command=new_game)
newButton.pack()

# Label Creation
lbl = tk.Label(root, text="")
lbl.pack()

for key in qwerty:
    if key == 'z':
        add(Keyboard, ' '+key, "Black")
    else:
        add(Keyboard, key, "Black")

tk.mainloop()
