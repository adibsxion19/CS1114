# Aadiba Haque
# CS - UY 1114
# 10 April 2020
#Lab 10 Problem 5

def is_sorted(lst):
    #list -->bool
    temp = lst[0]
    if lst == []:
        return True
    for element in lst:
        if temp <= element:
            increasing_order = True
        else:
            increasing_order = False
            return increasing_order
        temp = element
    return increasing_order


