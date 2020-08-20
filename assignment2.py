#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter as tk
from tkinter import font
""" """

blank_space=" "
workplaces = tk.Tk()
workplaces.title(20*blank_space+'Workplaces')
workplaces.geometry("300x175")
workplaces.configure(bg='white')
workplaces.resizable(width = False, height = False)

topframe=Frame(workplaces)
topframe.pack(side=TOP)
leftframe=Frame(topframe)
leftframe.pack(side=LEFT)
leftframe.config(bg="white")
rightframe=Frame(topframe)
rightframe.pack(side=RIGHT)
rightframe.config(bg="white")

def match():
    entry1.delete(0, 'end')
    pers =person.get(ANCHOR)
    workpl =workplace.get(ANCHOR)
    if (pers=='John Anderson' and workpl=='ABN Enterprises'):
            answer='CORRECT'
            
    elif (pers=='Yvonne Bryan' and workpl=='PLB Planet'):
            answer='CORRECT'
            
    elif (pers=='Peter Brown' and workpl=='Daily Radio'):
            answer='CORRECT'
            
    elif (pers=='Rick Grant' and workpl=="Rick's Cafe"):
            answer='CORRECT'
            
    elif (pers=='William Clarke' and workpl=='EKY Factory'):
            answer='CORRECT'
    else:
            answer='FALSE'
        
    return entry1.insert(0,answer)


label1 = tk.Label(leftframe, text='Person')
label1.config(bg="white")
person = Listbox(leftframe, width=15, height=5,bd=1,highlightbackground="black", exportselection=0)
    
person.insert(0, "John Anderson")
person.insert(1, "Yvonne Bryan")
person.insert(2, "Peter Brown")
person.insert(3, "Rick Grant")
person.insert(4, "William Clarke")
label1.pack()
person.pack(padx=10)
    
label2 = tk.Label(rightframe, text='Workplace')
label2.config(bg="white")
workplace = Listbox(rightframe, width=21, height=5,bd=1,highlightbackground="black", exportselection=0)
    
workplace.insert(0, "ABN Enterprises")
workplace.insert(1, "Daily Radio")
workplace.insert(2, "EKY Factory")
workplace.insert(3, "PLB Planet")
workplace.insert(4, "Rick's Cafe")
label2.pack()
workplace.pack(padx=10)

bottomframe=Frame(workplaces)
bottomframe.pack(side=BOTTOM)
bottomframe.config(bg="white")

button1=tk.Button(bottomframe, text='Determine if Match is Correct', height=1, width=23, command=match)
button1.config(bg="white")
button1.pack()

label3 = tk.Label(bottomframe, text='Answer:' )
label3.config(bg="white")
label3.pack(padx=5, pady=5, side=tk.LEFT)

entry1=Entry(bottomframe, text=' ',borderwidth=2, relief="groove", width=10 )
entry1.pack(padx=5, pady=5, side=tk.LEFT)

   


workplaces.mainloop()
