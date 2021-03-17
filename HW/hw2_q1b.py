# Author: Aadiba Haque
# Assignment / Part: HW2 - Q1 Part B
# Date due: 2020-02-21
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import math
weight = float(input("Please enter weight in pounds: "))
height = float(input("Please enter height in inches: "))

lb_to_kg = 0.453592 
inch_to_meter = 0.0254

weight_metric = weight * lb_to_kg
height_metric = height * inch_to_meter

BMI = weight_metric / math.pow(height_metric, 2)

print("BMI is:", BMI)