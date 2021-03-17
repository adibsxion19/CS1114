# Author: Aadiba Haque
# Assignment / Part: HW2 - Q3
# Date due: 2020-02-21
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import math
import turtle
a = float(input("Please enter length of one side of a triangle: "))
b = float(input("Please enter length of other side of the triangle: "))
angle = float(input("Please enter angle in degrees between the edges of the sides: "))
c = math.sqrt(math.pow(a, 2) + math.pow(b,2) - (2*a*b*math.cos(math.radians(angle))))

angle_1 = 180 - angle
angle_2 = 180 - math.degrees(math.acos((math.pow(c,2) + math.pow(b,2)-math.pow(a,2))/(2*c*b)))


turtle.forward(a)
turtle.left(angle_1)
turtle.forward(b)
turtle.left(angle_2)
turtle.forward(c)
                   