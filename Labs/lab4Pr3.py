# Aadiba Haque
# CS - UY 1114
# 21 February 2020
#Lab 4 Problem 3

import turtle

direction = input("Please enter a direction (R or L): ")
side_length = int(input("Please enter a side length: "))

angle_turn_l = 240

angle_turn_r = 60
angle_turn = 120

if direction == "R":
    turtle.right(angle_turn_r)
    turtle.forward(side_length)
    turtle.right(angle_turn)
    turtle.forward(side_length)
    turtle.right(angle_turn)
    turtle.forward(side_length)
    
if direction == "L":
    turtle.left(angle_turn_l)
    turtle.forward(side_length)
    turtle.left(angle_turn)
    turtle.forward(side_length)
    turtle.left(angle_turn)
    turtle.forward(side_length)

