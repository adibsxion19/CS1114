# Author: Aadiba Haque
# Assignment / Part: HW5 - Q3
# Date due: 2020-03-13
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic

string = input("Enter a string: ")

print("Your string case swapped is: ", end ="")
for every_char in string:
    if every_char == every_char.upper():
        print(every_char.lower(),end = '')
    elif every_char == every_char.lower():
        print(every_char.upper(),end = '')