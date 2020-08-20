#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randrange

""" """
username= 'uname'
password= 'passw'
wins=0
losses=0
ties=0

def authentication():
    a=randrange(10)
    b=randrange(10)
    
    ans=a+b

    print(a,"+", b,"? ")
    results=int((input()))

    if(ans!=results):
        print("You entered the wrong number in captcha")
    else:
        print("Login Successful")
        game()

def userlogin():
    i=0
    for i in range(3):
        unam=(input("Enter Login ID:"))
        pword=(input("Enter password: "))
        if(username==unam and password==pword):
            authentication()
            
            
        else:
            print("Try Again")
        i=i+1
    exit()
def game():
    menu = {}
    menu['1']="File." 
    menu['2']="Rules."
    menu['3']="Restart"
    while True:
        options=menu.keys()
        print("Menu:")
        for entry in options:
            
            print (entry, menu[entry])

        selection=input("Please Select:") 
        if selection =='1': 
            print ("add" )
        elif selection == '2': 
            print ("The rules of the game is as follows. \nYou can choose between rock, paper and scissors. \nRock beats scissors, Paper beats rock, and Scissors beats paper.")
        elif selection == '3':
            main()
        else: 
            print ("Unknown Option Selected!" )

def main():
	"""Launcher."""
	userlogin()
	pass
 
if __name__ == "__main__":
	main()
