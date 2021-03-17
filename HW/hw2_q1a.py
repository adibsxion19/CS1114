# Author: Aadiba Haque
# Assignment / Part: HW2 - Q1 Part A
# Date due: 2020-02-21
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import math
weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))

BMI = weight / math.pow(height, 2)

print("BMI is: ", BMI)
