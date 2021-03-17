# Aadiba Haque
# CS - UY 1114
# 10 April 2020
#Lab 10 Problem 3

def sum_some(num1, num2,lst):
    #sig: int, int, list --> int
    sum_elements = 0
    for element in lst:
        if element in range(num1,num2+1):
            sum_elements += element
    return sum_elements

