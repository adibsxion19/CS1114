# Author: Aadiba Haque
# Assignment / Part: HW5 - Q1 
# Date due: 2020-03-13
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.


string = input("Please enter a string:")
function = True

for every_char in string:
    if every_char.isalpha() and every_char > 'Z':
        new_char = every_char
    elif every_char.isalpha() == False:
        new_char = every_char
    else:
        new_char = chr(ord(every_char) + (ord('a')-ord('A')))
    print(new_char, end = '')
    
