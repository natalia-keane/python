#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
"""A men’s clothing store advertises that if you buy a suit, you can get a second suit at half-off.
What they mean is that if you buy two suits, then the price
of the lower-cost suit is reduced by 50%. Write a program that accepts	the two costs as
input and then calculates the total cost after halving	the cost of the lowest price suit."""
 
def half_off():
    cost=0.0

    suit1 = float(input("Enter cost of first suit: "))
    suit2 = float(input("Enter cost of second suit: "))
  
    
    if suit1>suit2:
        cost=.5*suit2+suit1
        bals="${:.2f}.".format(float(cost))
        print("Cost of the two suits is",bals)
    else:        
        cost=.5*suit1+suit2
        bals="${:.2f}.".format(float(cost))
        print("Cost of the two suits is",bals)
 
def main():
	"""Launcher."""
	half_off()
	pass
 
if __name__ == "__main__":
	main()
