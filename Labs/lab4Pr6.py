# Aadiba Haque
# CS - UY 1114
# 21 February 2020
#Lab 4 Problem 6

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
        
if a > b and a > c and a**2 == (b**2) + (c**2):
    print("It is possible to make a triangle with the side lengths",str(a),",",str(b),", and",str(c))
if b > a and b > c and b**2 == (a**2) + (c**2):    
    print("It is possible to make a triangle with the side lengths",str(a),",",str(b),",and",str(c))
if c > b and c > a and c**2 == (b**2) + (a**2):
    print("It is possible to make a triangle with the side lengths",str(a),",",str(b),",and",str(c))
else:
    print("It is not possible to make a triangle with the side lengths",str(a),",",str(b),",and",str(c))