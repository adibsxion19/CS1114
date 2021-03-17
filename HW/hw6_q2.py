# Author: Aadiba Haque
# Assignment / Part: HW6 - Q2 
# Date due: 2020-04-03
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import turtle
def n_pointed_star(n_points):
    #sig: int
    counter = 0
    outer_angle_of_turn = 2* (360/n_points)
    inner_angle_of_turn =  360/n_points
    start_angle = 360/ n_points
    turtle.left(start_angle)
    while counter < n_points:
        turtle.forward(100)
        turtle.left(inner_angle_of_turn) 
        turtle.forward(100)
        turtle.right(outer_angle_of_turn)
        counter += 1
        
def main():
    n_points = int(input("How many points will the star have? "))
    n_pointed_star(n_points)

main()