# Author: Aadiba Haque
# Assignment / Part: HW3 - Q4
# Date due: 2020-02-28
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import math 

a = float(input("Please enter value of a:"))
b = float(input("Please enter value of b:"))
c = float(input("Please enter value of c:"))

discriminant = (math.pow(b,2))-(4*a*c)

if a != 0:
    if discriminant == 0:
        x = ((-1 * b) + math.sqrt(discriminant))/(2*a)
        print("This equation has a single real solution x=", x1)
    if discriminant > 0:
        x1 = ((-1 * b) + math.sqrt(discriminant))/(2*a)
        x2 = ((-1 * b) - math.sqrt(discriminant))/(2*a)
        print("This equation has two real solutions x=", x1, "and x=", x2)

if discriminant < 0:
    print("This equation has no real solutions.")
    
if a == 0:
    if b == 0 and c == 0:
        print("This equation has an infinite number of solutions.")
    else:
        print("This equation has no solution.")