#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
""" Write a program to process	a savings-account withdrawal.
The programshould request the current balance and the amount of the withdrawal as input and
then display the new balance If the withdrawal is greater than the original balance, the
program	should display	“Withdrawal denied." If the new	balance	is less	than $150, the
message	“Balance below 150” should also	be displayed."""
 

def withdraw():
    
    newbal=0.0
    bal = float(input("Enter current balance: "))
    amt = float(input("Enter amount of withdrawal: "))
    
    newbal=bal-amt
    if amt>bal:
        print("Withdrawal denied.")
    elif newbal<150:
        print("Balance below $150")
    else:
        newbals="${:.2f}.".format(float(newbal))
        print("The new balance is",newbals)
 
def main():
	"""Launcher."""
	withdraw()
	pass
 
if __name__ == "__main__":
	main()
