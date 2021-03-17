# Author: Aadiba Haque
# Assignment / Part: HW5 - Q4
# Date due: 2020-03-13
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic

string = input("Enter a string to modify: ")
index_and_char = input("Enter an index value and a character: ")


index_val = int(index_and_char[0])
new_string = string[:index_val] + index_and_char[2] + string[index_val+1:]
print("Your modified string is: " + new_string)