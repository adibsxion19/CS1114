# Author: Aadiba Haque
# Assignment / Part: HW4 - Q6a
# Date due: 2020-03-06
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

length_of_seq = int(input("Please enter the length of the sequence: "))
print("Please enter your sequence: ")

user_input = 0
counter = 1
multiply_value = 1

while counter <= length_of_seq:
    user_input = int(input())
    multiply_value *= user_input
    counter += 1
    
geometric_mean = multiply_value**(1/length_of_seq)
        
print("The geometric mean is: ", round((geometric_mean),4))



    
    
    
    
    
    
    