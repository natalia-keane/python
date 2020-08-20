#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter as tk
from tkinter import font
import random
from tkinter import messagebox

#Load and show an image with Pillow from PIL import Image

""" pip install pmw; pip install pillow

#Load the image
img = Image.open('rock.jpg')
img.show()"""

wins=0
losses=0
ties=0
options=['Rock', 'Paper', 'Scissors']

def rules():
    """This function displays the rules f the game as an alert"""
    messagebox.showinfo("Rules", "The rules of the game is as follows. \nYou can choose between rock, paper and scissors. \nRock beats scissors, Paper beats rock, and Scissors beats paper.")
  

def compare():
    """ This function controls the game and keeps record of the scores"""
    global wins
    global losses
    global ties
    compentry.delete(0, 'end')
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    userchoice=v.get()
    compchoice=random.choice(options)
    if losses<10 and wins<10:
        if userchoice==compchoice:
            ties=ties+1
            
        elif userchoice=='Rock' and compchoice=='Scissors':
            wins=wins+1
            
        elif userchoice=='Scissors' and compchoice=='Paper':
            wins=wins+1
            
        elif userchoice=='Paper' and compchoice=='Rock':
            wins=wins+1
            
        else:
            losses=losses+1
        return (compentry.insert(0,compchoice),entry1.insert(0,wins),entry2.insert(0,losses),entry3.insert(0,ties))

chalenge = tk.Tk()
chalenge.title("Battle System")
chalenge.geometry("450x400")
chalenge.configure(bg='white')
chalenge.resizable(width = False, height = False)
v = StringVar()

topframe=Frame(chalenge)
topframe.pack(side=TOP)

leftframe=Frame(topframe, highlightbackground='black', highlightthickness=1)
leftframe.pack(side=BOTTOM )

rightframe=Frame(chalenge)
rightframe.pack(side=RIGHT)

bottomframe=Frame(chalenge)
bottomframe.pack(side=BOTTOM)

blframe=Frame(bottomframe,highlightbackground='black', highlightthickness=1)

blframe.pack(side=LEFT)

head1=tk.Button(topframe, text='File')
head3=tk.Button(topframe, text='Restart')
head2=tk.Button(topframe, text='Rules', command=rules)

head1.pack(padx=5, pady=10, side=tk.LEFT)
head2.pack(padx=5, pady=20, side=tk.LEFT)
head3.pack(padx=5, pady=20, side=tk.LEFT)

inst1 = tk.Label(rightframe, text='Rock beats Scissors, Paper beats Rock, and Scissors beats Paper.')
inst1.pack(fill=tk.X)
label1 = tk.Label(leftframe, text='Choice')

label1.pack()
Radiobutton(leftframe, 
              text="Rock",
              padx = 20, 
              variable=v, 
              value="Rock").pack(anchor=W)
Radiobutton(leftframe, 
              text="Paper",
              padx = 20, 
              variable=v, 
              value="Paper").pack(anchor=W)
Radiobutton(leftframe, 
              text="Scissors",
              padx = 20, 
              variable=v, 
              value="Scissors").pack(anchor=W)

 
label2 = tk.Label(blframe, text='Scores')

label3 = tk.Label(blframe, text='Wins:')

label4 = tk.Label(blframe, text='Losses:')

label5 = tk.Label(blframe, text='Ties:')


button1=tk.Button(rightframe, text='Attack', command=compare)
clabel=tk.Label(rightframe, text="The Computer chose:")

compentry=Entry(rightframe, text='',borderwidth=2, relief="groove", width=10 )

entry1=Entry(blframe, text='',borderwidth=2, relief="groove", width=2 )

entry2=Entry(blframe, text='',borderwidth=2, relief="groove", width=2 )

entry3=Entry(blframe, text='',borderwidth=2, relief="groove", width=2)


label2.pack()
label3.pack()
label4.pack()
label5.pack()
entry1.pack()

entry2.pack()

entry3.pack()

clabel.pack()
compentry.pack(padx=40, pady=5)
button1.pack(pady=5)

chalenge.mainloop()
