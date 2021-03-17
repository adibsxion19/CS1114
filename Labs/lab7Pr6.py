# Aadiba Haque
# CS - UY 1114
# 13 March 2020
#Lab 7 Problem 6

string1 = input("Enter String 1: ")
string2 = input("Enter String 2: ")

counter = 0
for i in range(len(string1)):
    if string1[i] != string2[i]:
        counter += 1
print(counter)

