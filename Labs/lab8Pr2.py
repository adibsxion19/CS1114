# Aadiba Haque
# CS - UY 1114
# 27 March 2020
#Lab 8 Problem 2
def replace_spaces(s):
    #sig: str --> str
    acc = ''
    for char in s:
        if char == ' ':
            new_char = '_'
        else:
            new_char = char
        acc += new_char
    print(acc)
    return acc



