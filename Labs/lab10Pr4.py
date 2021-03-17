# Aadiba Haque
# CS - UY 1114
# 10 April 2020
#Lab 10 Problem 4

def my_count(lst, val):
    #sig: list(int), int --> int
    counter = 0
    for element in lst:
        if val == element:
            counter += 1
    return counter
