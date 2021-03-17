# Author: Aadiba Haque
# Assignment / Part: HW5 - Q5
# Date due: 2020-03-13
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic


inOrder = False

while inOrder == False:
    temp = -1
    number = input("Please enter a six-digit number in order: ")
    Correct = True

    for digit in number:
        if int(digit) > temp:
            temp = int(digit)
        else:
            Correct = False
  
    if Correct == True:
        inOrder = True 

    

    

