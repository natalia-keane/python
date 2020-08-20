#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
""" Saving Account. \Write a Pseudo-code and Python menu-driven program that
allows the user to make transactions to a
savings account. Assume that the account initially has a balance of $1,000."""

bal = 1000

def deposit():
    
    global bal
    
    amt = float(input("Enter amount of deposit: "))
    
    bal=bal+amt
    print("The new balance is",bal)
    return bal
def balance():
    
    print("Current balance is:", bal)
    return bal
        
def withdraw():
    
    global bal
    
    amt = float(input("Enter amount of withdrawal: "))
    bal=bal-amt
    print("The new balance is",bal)
    return bal

def menu():
    while True:
        print("\nMenu\n(V)iew Balance\n(D)eposit Funds\n(W)ithdraw Funds\n(Q)uit")
        choice = input(">>> ").lower().rstrip()
        if choice=="q":
            break
        elif choice=="v":
            balance()
        elif choice=="d":
            deposit()
        elif choice=="w":
            withdraw()
        else:
            print("Invalid choice, please choose again\n")



 
def main():
	"""Launcher."""
	menu()
	pass
 
if __name__ == "__main__":
	main()
