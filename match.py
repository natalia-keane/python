#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
"""A men’s clothing store advertises that if you buy a suit, you can get a second suit at half-off.
What they mean is that if you buy two suits, then the price
of the lower-cost suit is reduced by 50%. Write a program that accepts	the two costs as
input and then calculates the total cost after halving	the cost of the lowest price suit."""
 
def match():
    pers = input("Enter cost of first suit: ")
    workpl = input("Enter cost of first suit: ")
    if (pers=='John Anderson' and workpl=='ABN Enterprises'):
        answer='Correct'
    elif (pers=="Yvonne Bryan" and workpl=="PLB Planet"):
        answer='Correct'
    elif (pers=="Peter Brown" and workpl=="Daily Radio"):
        answer='Correct'
    elif (pers=="Rick Grant" and workpl=="Rick's Cafe"):
        answer='Correct'
    elif (pers=="William Clarke" and workpl=="EKY Factory"):
        answer='Correct'
    else:
        answer='False'
    return print(answer)

def main():
	"""Launcher."""
	match()
	pass
 
if __name__ == "__main__":
	main()
