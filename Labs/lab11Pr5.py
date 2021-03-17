# Aadiba Haque
# CS - UY 1114
# 17 April 2020
#Lab 11 Question 5
def find_room(room_lst,name_lst):
    #sig: list(tuples),list(strings) --> list(lists)
    resulting_list = []
    for value in range(len(room_lst)):
        resulting_list.append([])
    for element in name_lst: 
        for rooms in range(len(room_lst)):
            if room_lst[rooms][0] <= element <= room_lst[rooms][1]:
                resulting_list[rooms].append(element)
    return resulting_list
print(find_room([("Aa","Mz"),("Na", "Za")],["Gordon","Ypsilon","Lightyear","Skywalker"]))
print(find_room([("Aa","Mz"),("Na", "Za")],["Aardvark","Zuniga"]))
        