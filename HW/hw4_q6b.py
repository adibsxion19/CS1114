# Author: Aadiba Haque
# Assignment / Part: HW4 - Q6b
# Date due: 2020-03-06
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

print('''Please enter a non-empty sequence of positive
integers, each one on a separate line. End your
sequence by typing done.''')
user_input = input()

counter = 0
multiply_value = 1
while user_input != 'done':
    counter += 1
    multiply_value *= int(user_input)
    user_input = input()
    
geometric_mean = (multiply_value)**(1/counter)
print("The geometric mean is: ", round(geometric_mean,4))
    
