# Aadiba Haque
# CS - UY 1114
# 13 March 2020
#Lab 7 Problem 5

password = input("Please enter a password: ")

for every_char in password:
    if every_char == every_char.upper():
        Valid = True
    elif every_char == every_char.lower():
        Valid = True
    elif every_char ==  '0' or every_char ==  '1' or every_char ==  '2' or every_char =='3' or every_char == '4' or every_char = '5' or every_char = '6' or every_char = '7' or every_char = '8' or every_char = '9':
        Valid = True
    elif every_char == '!' or every_char == '@' or every_char == "#" or every_char == "$":
        Valid = True
    else:
        Valid = False
        
if every_char == True:
    print("True")
else:
    print("False")
    