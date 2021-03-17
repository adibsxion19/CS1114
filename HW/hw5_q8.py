# Author: Aadiba Haque
# Assignment / Part: HW5 - Q8
# Date due: 2020-03-13
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic

text = input("Please enter a line of text: ")
ch = input("Please enter a character you want to remove: ")


for letter in text:
    if letter == ch:
        continue
    else:
        print(letter, end = '')
