# Aadiba Haque
# CS - UY 1114
# 10 April 2020
#Lab 10 Problem 2
def avg (numbers) :
    #sig: list(float) --> float
    total = 0
    for element in numbers:
        total += element
    if numbers != []:
        average = total / len(numbers)
        return average


