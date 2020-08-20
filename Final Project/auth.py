#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from tkinter import messagebox
from random import randrange
from tkinter import *
import tkinter as tk
window = tk.Tk()
window.title("Authentication")
window.geometry("500x150")


       

def authentication():
    def authcheck():
        if(ans!=int(entry1.get())):
            messagebox.showinfo("Captcha", "You entered the wrong captcha")
            '''print("You entered the wrong number in captcha")'''
        else:
            messagebox.showinfo("Captcha", "You entered the correct captcha")
            '''print("Correct")'''
    
    
    a=randrange(10)
    b=randrange(10)
    ans=a+b
    say=(a,"+", b,"? ")
    root = tk.Tk()
    root.title("Captcha Quiz")
    root.geometry("300x150")
    t = tk.Label(root, text=say)
    t.pack()
    
    '''print(a,"+", b,"? ")'''
    '''results=int((input()))'''
    entry1=Entry(root, text='',borderwidth=2, relief="groove", width=5 )
    entry1.pack()
    
    entry1.delete(0, 'end')
    button1=tk.Button(root, text='OK', command=authcheck)
    button1.pack()
    
    

startButton = tk.Button(window, command=authentication, text="Captcha")
startButton.pack()
window.mainloop()    

