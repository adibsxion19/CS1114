# Aadiba Haque
# CS - UY 1114
# 28 February 2020
#Lab 5 Problem 4

n = int(input("Please enter a number: "))
x=0


while n % 10 != 0:  
    x += n % (10)
    n = n//10
x += n
print(x)
    
    




    
    
    
    
    