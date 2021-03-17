# Aadiba Haque
# CS - UY 1114
# 13 March 2020
#Lab 7 Problem 4

string = input("Enter a string, consisting of only the digits 1 and 0: ")
zeros = ones = 0
temp =''

for digit in string:
    if digit == '0' and temp == '1':
        zeros = len(string[:string.find(digit)+1])
        print(zeros, "1's")
    if digit == '1' and temp == '0':
        ones = len(string[:string.find(digit)+1])
        print(ones, "0's")    
    temp = digit



    
    

    
    
    
