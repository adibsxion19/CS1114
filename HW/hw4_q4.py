# Author: Aadiba Haque
# Assignment / Part: HW4 - Q4
# Date due: 2020-03-06
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

pos_int_n = int(input("Please enter a positive integer: "))
#old_num is the value for the previous row
#new_num is the value for the current row
#row_num is what # row the current output is at

old_num = 0
row_num = 1

while row_num <= pos_int_n:
    new_num = row_num
    new_num += old_num 
    print(" "*(pos_int_n - row_num), new_num)
    old_num = new_num * 10
    row_num += 1
     