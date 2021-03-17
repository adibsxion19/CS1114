# Author: Aadiba Haque
# Assignment / Part: HW7 - Q2 
# Date due: 2020-04-17
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import random
def shuffle(lst):
    # sig:list --> list
    prev_index = []
    new_lst = []
    for element_index in range(len(lst)):
        random_index = random.randint(0, len(lst)-1)
        while (random_index in prev_index) or element_index == random_index:
            random_index = random.randint(0, len(lst)-1)
        else:
            new_lst.append(lst[random_index])
            prev_index.append(random_index)
    return new_lst
def main():
    print(shuffle([True, 1, "hello",4.0,[1,"pop",False],9,"bye"]))
    
main()
