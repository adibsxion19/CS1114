# Aadiba Haque
# CS - UY 1114
# 10 April 2020
#Lab 10 Problem 7

def count_digits(val):
    # sig : int -> lst (int)
    count_lst = [0] * 10
    for digit in str(val):
        count_lst[int(digit)] += 1
    return count_lst

def print_digits(lst):
    # sig : list(int) -> NoneType
    for i in range(len(lst)):
        if lst [ i ] > 0:
            print (i , "appears" , lst[i] , "times")

def main():
   print_digits(count_digits())

main()

