# Author: Aadiba Haque
# Assignment / Part: HW4 - Q5
# Date due: 2020-03-06
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

pos_int_n = int(input("Please enter a positive integer: "))

for num in range(1,pos_int_n+1):  
    even_digit = 0
    odd_digit = 0
    digit = num
    while digit != 0:
        last_digit = digit % 10
        digit = digit // 10
        if last_digit % 2 == 0:
            even_digit += 1
        else:
            odd_digit += 1

    if even_digit > odd_digit:
        print(num, end = " ")



