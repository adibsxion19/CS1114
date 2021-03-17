# Aadiba Haque
# CS - UY 1114
# 21 February 2020
#Lab 4 Problem 4

time = int(input("Please enter the time in 24hr format: "))

minute = time % 100

hour = time // 100

if hour == 12:
    print (str(hour).zfill(2)+":"+str(minute).zfill(2)+"pm")

if hour == 0:
    hour = 12
    print(str(hour).zfill(2)+":"+str(minute).zfill(2)+"am")

elif hour > 12:
    hour -= 12
    print (str(hour).zfill(2)+":"+str(minute).zfill(2)+"pm")

elif hour < 12:
    print(str(hour).zfill(2)+":"+str(minute).zfill(2)+"am")
    

