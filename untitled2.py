# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 16:37:10 2022

@author: shn99
"""

from tkinter import *
import random

root=Tk()

root.title("Random Word Generator")
root.geometry("500x500")


list1 = ["a" , "b" , "c" , "d" , "e","f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(list1)

def random_number():
    def random_no():
        random_no = random.randint(1, 26)
random_no1 = random.randint(1, 26)
random_no2 = random.randint(1, 26)
random_no3 = random.randint(1, 26)
random_no4 = random.randint(1, 26)
print(random_no)
print(random_no1)
print(random_no2)
print(random_no3)
print(random_no4)
random_lucky_word = list1[random_no]
print("Your random word is is: " + random_lucky_word)


btn1 = Button(root, text="Who is your Lucky Friend?  ", command = random_number)
btn1.place(relx= 0.5,rely = 0.5, anchor = CENTER )

root.mainloop()