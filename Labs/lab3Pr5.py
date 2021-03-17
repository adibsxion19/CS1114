# Aadiba Haque
# CS - UY 1114
# 14 February 2020
#Lab 3 Problem 5


import turtle
import math

base_side = 100
base_angle = 72
side_triangle = (base_side / 2) / math.cos(math.radians(base_angle))
angle_star = 144

# Part 1
# turtle.forward(side_triangle)
# turtle.penup()
# turtle.forward(base_side)
# turtle.pendown()
# turtle.forward(side_triangle)
# turtle.right(angle_star)
# turtle.forward(side_triangle)
# turtle.penup()
# turtle.forward(base_side)
# turtle.pendown()
# turtle.forward(side_triangle)
# turtle.right(angle_star)
# turtle.forward(side_triangle)
# turtle.penup()
# turtle.forward(base_side)
# turtle.pendown()
# turtle.forward(side_triangle)
# turtle.right(angle_star)
# turtle.forward(side_triangle)
# turtle.penup()
# turtle.forward(base_side)
# turtle.pendown()
# turtle.forward(side_triangle)
# turtle.right(angle_star)
# turtle.forward(side_triangle)
# turtle.penup()
# turtle.forward(base_side)
# turtle.pendown()
# turtle.forward(side_triangle)

#Part 2
turtle.forward(side_triangle)
turtle.left(base_angle)
turtle.forward(side_triangle)
turtle.right(angle_star)
turtle.forward(side_triangle)
turtle.left(base_angle)
turtle.forward(side_triangle)
turtle.right(angle_star)
turtle.forward(side_triangle)
turtle.left(base_angle)
turtle.forward(side_triangle)
turtle.right(angle_star)
turtle.forward(side_triangle)
turtle.left(base_angle)
turtle.forward(side_triangle)
turtle.right(angle_star)
turtle.forward(side_triangle)
turtle.left(base_angle)
turtle.forward(side_triangle)
turtle.right(angle_star)
