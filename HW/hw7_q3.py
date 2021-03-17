# Author: Aadiba Haque
# Assignment / Part: HW7 - Q3
# Date due: 2020-04-17
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

def weave(list1,list2):
    #sig:list, list --> list
    index = 0
    resulting_list =[]
    if len(list1) >= len(list2):
        while index < len(list1):
            resulting_list.append(list1[index])
            if index < len(list2):
                resulting_list.append(list2[index])
            index += 1
    elif len(list1) < len(list2):
        while index < len(list2):
            if index < len(list1):
                resulting_list.append(list1[index])
            resulting_list.append(list2[index])
            index += 1
    return resulting_list

def main():
    print(weave(["joe","tom","penny","sue"],[5,20,35,15]))
    print(weave(["joe","tom","penny","sue"],[5,20]))
main()
