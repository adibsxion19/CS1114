# Author: Aadiba Haque
# Assignment / Part: HW5 - Q7 Part B
# Date due: 2020-03-13
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic

decimal = int(input("Please enter a decimal number: "))
orig_dec = decimal
num_of_M = num_of_D = num_of_C = num_of_L = num_of_X = num_of_V = num_of_I = 0

num_of_M = decimal // 1000
decimal -= num_of_M * 1000

num_of_D = decimal // 500
decimal -= num_of_D * 500  

num_of_C = decimal // 100
decimal -= num_of_C* 100

num_of_L = decimal // 50
decimal -= num_of_L*50

num_of_X = decimal // 10
decimal -= num_of_X* 10

num_of_V = decimal // 5
decimal -= num_of_V*5

num_of_I = decimal
decimal -= num_of_I
    
print(orig_dec, 'is', num_of_M*'M' + num_of_D*'D' + num_of_C*'C' + num_of_L *'L' + num_of_X *'X' + num_of_V *'V' +num_of_I*'I')

      
    