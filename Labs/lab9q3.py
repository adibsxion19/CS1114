# Aadiba Haque
# CS - UY 1114
# 3 March 2020
#Lab 9 Q3

def check_leap_year(year):
    #sig:int
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
            else:
                leap_year = False
        else:
            leap_year = True
    else:
        leap_year = False
    return leap_year

def main():
    leap_year = int(input("Please enter a year: "))
    print(check_leap_year(leap_year))

main()