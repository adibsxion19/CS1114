# Aadiba Haque
# CS - UY 1114
# 27 March 2020
#Lab 8 Problem 4

def title_case(s):
    #sig: str --> str
    previous_char = ''
    acc = ''
    for char in s:
        if previous_char == '' or previous_char == ' ' or (previous_char in "'.,;:?!"):
            acc += char.upper()
        else:
            acc += char
        previous_char = char
    print(acc)
    return acc

    

