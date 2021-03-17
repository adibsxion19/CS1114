# Author: Aadiba Haque
# Assignment / Part: HW3 - Q2
# Date due: 2020-02-28
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

item1 = float(input("Enter the price of the first item:"))
item2 = float(input("Enter the price of the second item:"))
card = input("Does the customer have a club card? (Y/N): ")
tax_rate = float(input("Enter the tax rate, e.g. 5.5 for 5.5% tax: "))

total = item1 + item2

print("Base price =", total)

if item1 > item2:
    item2 /= 2

if item2 > item1:
    item1 /= 2

total = item1 + item2
    
if card == "Y":
    total *= 0.90
    
print("Price after discounts =", total)

total *= (1+(tax_rate / 100))

print("Total Price =", round(total, 2))
