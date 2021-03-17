# Author: Aadiba Haque
# Assignment / Part: HW5 - Q2
# Date due: 2020-03-13
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

string = input("Please enter a sentence:")
counter = 0
for letter in range(ord('A'), ord('Z')+1):
    if string.upper().find(chr(letter)) == -1:
        missing_letter = chr(letter)
        print(missing_letter)
    else:
        counter +=1
if counter == 26:
    print("True")
     
    
    