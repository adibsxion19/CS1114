# Author: Aadiba Haque
# Assignment / Part: HW7 - Q6
# Date due: 2020-04-17
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

def encoder(string):
    #str --> list
    counter = 0
    prev_ch = string[0]
    lst = []
    new_string = string + ' '
    for ch in new_string:
        if prev_ch == ch:
            counter += 1
        else:
            lst.append([prev_ch,counter])
            counter = 1
        prev_ch = ch
    return lst
        
       
def decoder(lst):
    #list --> str
    string = ''
    for element in lst:
        string += (element[0] * element[1])
    return string

def main():
    string = input("Enter a string to be encoded: ")
    lst = encoder(string)
    string = decoder(lst)
    print("The encoded string is: ", lst)
    print("The decoded string resulting from the encoded string is: ", string)
main()