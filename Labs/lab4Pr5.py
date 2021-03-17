# Aadiba Haque
# CS - UY 1114
# 21 February 2020
#Lab 4 Problem 5

item1 = float(input("Price of Item 1:"))
item2 = float(input("Price of Item 2:"))
card = input("Club Card Member (Y/N): ")
tax_rate = float(input("Tax: "))


if item1 > item2:
    item2 /= 2

if item2 > item1:
    item1 /= 2

total = item1 + item2
    
if card == "Y":
    total *= 0.90

total *= (1+(tax_rate / 100))

print("Total Price: $"+ str(total))
