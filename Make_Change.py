#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
"""A supermarket sells	apples	for $2.50 per	pound.	Write a	cashier’s	
program	that requests the number of pounds and	the amount of cash tendered as	input	
and displays the change	from the transaction. If the cash is not enough, the message "You	
owe $x.xx more." should	be displayed, where $x.xx is the difference between the total cost	
and the	cash."""
 
def cash():
    cost=0.0
    apple=2.50
    weight = float(input("Enter weight in pounds: "))
    money = float(input("Enter payment in dollars: "))
    cost=apple*weight
    
    if cost>money:
        remainder=cost-money
        bals="${:.2f}".format(float(remainder))
        print("You owe",bals,"more.")
    elif cost<money:
        remainder=money-cost
        bals="${:.2f}.".format(float(remainder))
        print("Your change is",bals)
    
 
def main():
	"""Launcher."""
	cash()
	pass
 
if __name__ == "__main__":
	main()
