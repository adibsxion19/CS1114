# Author: Aadiba Haque
# Assignment / Part: HW5 - Q6
# Date due: 2020-03-13
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic

string = input("Please enter a string of lowercase letters: ")

temp = ''

for letter in string:
    if letter < temp:
        decreasing = True  
    else:
        decreasing = False
    temp = letter
    
if decreasing == True:
    print(string, "is decreasing.")
else:
    print(string, "is not decreasing.")