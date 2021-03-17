# Aadiba Haque
# CS - UY 1114
# 28 February 2020
#Lab 5 Problem 3

dividend = int(input("Enter the Dividend:"))
divisor = int(input("Enter the Divisor:"))

i = dividend
counter = 0

while i >= divisor:  
    i -= divisor
    counter += 1
    if i < divisor:
        print(counter, "R", i)
    