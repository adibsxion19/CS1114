# Author: Aadiba Haque
# Assignment / Part: HW7 - Q7
# Date due: 2020-04-17
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

def reverse_to_new_list(lst1):
    new_list = []
    for element in lst1[::-1]:
        new_list.append(element)
    return new_list
def reverse_in_place(lst2):
    lst2[:] = lst2[::-1]
    return lst2
def main():
    lst1 = [1, 2, 3, 4, 5, 6]
    rev_lst1 = reverse_to_new_list(lst1)
    print("After reverse_to_new_list, lst1 is", lst1, "and the returned list is", rev_lst1)
    
    lst2 = [1, 2, 3, 4, 5, 6]
    print("Before reverse_in_place, lst2 is", lst2)
    reverse_in_place(lst2)
    print("After reverse_in_place, lst2 is", lst2)

main()