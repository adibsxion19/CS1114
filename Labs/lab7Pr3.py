# Aadiba Haque
# CS - UY 1114
# 13 March 2020
#Lab 7 Problem 3

DNA_sequence = 'ACTGATCGATTAGCAGTAAGCGCTTAGCT'
for letter in DNA_sequence:
    if letter == 'A':
        complement_letter = 'T'
    elif letter == 'T':
        complement_letter = 'A'
    elif letter == 'C':
        complement_letter = 'G'
    elif letter == 'G':
        complement_letter = 'C'
    print(complement_letter, end = '')