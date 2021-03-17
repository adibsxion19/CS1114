# Author: Aadiba Haque
# Assignment / Part: HW7 - Q5
# Date due: 2020-04-17
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

def create_prefix_lists(lst):
    big_list = []
    for index in range(len(lst)+1):
        big_list.append(lst[:index])
    return big_list        

def main():
    print(create_prefix_lists([2, 4, 6, 8, 10]))

main()

