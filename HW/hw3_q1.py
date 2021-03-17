# Author: Aadiba Haque
# Assignment / Part: HW3 - Q1
# Date due: 2020-02-28
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import math
weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))

BMI = weight / math.pow(height, 2)

if 18.5 > BMI:
    print("BMI is: Underweight")

if  24.9 >= BMI >= 18.5:
    print("BMI is: Normal")

if  29.9 >= BMI >= 25.0:
    print("BMI is: Overweight")

if  BMI >= 30.0:
    print("BMI is: Obese")