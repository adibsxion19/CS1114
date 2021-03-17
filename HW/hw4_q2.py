# Author: Aadiba Haque
# Assignment / Part: HW4 - Q2 
# Date due: 2020-03-06
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

n = int(input("Please enter a positive integer: "))
start = 2*n-1
counter = 0
for i in range(start,1,-2):
    print(' '*counter + '*'*i)
    counter += 1
    
for i in range(1,start+1,2):
    print(' '*counter +'*'*i)
    counter -= 1
   