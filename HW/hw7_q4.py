# Author: Aadiba Haque
# Assignment / Part: HW7 - Q4
# Date due: 2020-04-17
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

def add_list(list1, list2):
    #sig: list(int),list(int)-->list(int)
    index = 0
    new_list =[]
    while index < len(list1):
        addition = list1[index] + list2[index]
        new_list.append(addition)
        index += 1
    return new_list

def main():
    print('Please enter a list of numbers, one per line, ending with a line "done" when the list is completed.')
    element = input()
    list1 =[]
    while element != 'done':
       list1.append(float(element))
       element = input()
    print('Please enter a list of numbers, one per line, ending with a line "done" when the list is completed.')
    element = input()
    list2 =[]
    while element != 'done':
        list2.append(float(element))
        element = input()
    if len(list1) != len(list2):
        print("The lists are different lengths.")
    else:
        print(add_list(list1,list2))
main()


