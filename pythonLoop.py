#!/usr/bin/python
# -*- coding: latin-1 -*-

run_loop = True

while run_loop == True:
    num = input("Enter a number: ")
    if num.isnumeric():
        print("Yes, it's a number.")
    else:
        print("Not a number.")
        run_loop = False
