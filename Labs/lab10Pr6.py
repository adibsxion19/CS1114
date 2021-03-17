# Aadiba Haque
# CS - UY 1114
# 10 April 2020
#Lab 10 Problem 6

def get_common_elems(lst1, lst2):
    #sig : list(int),list(int) -> list(int)
    return_list = []
    for element in lst1:
        if element in lst2:
            return_list.append(element)
    return return_list

