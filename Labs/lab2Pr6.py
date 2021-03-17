# Aadiba Haque
# CS - UY 1114
# 7 February 2020
#Lab 2 Problem 6
birth = int(input("Please enter a date of birth: "))
day = birth%100
month = (birth//100)%100
year = (birth//10000)

today = int(input("Please enter today's date: "))
day1 = today%100
month1 = (today//100)%100
year1 = (today//10000)
print("Date of birth is "+ str(month)+"/"+str(day)+ "/"+str(year))
print("Today's date is "+str(month1)+"/"+str(day1)+"/"+ str(year1))

sub_y = year1 - year
sub_m = month1 - month
sub_d = day1 - day
how_long = 360*sub_y +30*sub_m + sub_d
year = how_long //360
month = (how_long % 360)//30
day = (how_long %360)%30
print("You have been alive for ",str(year),"years", str(month),"months",str(day),"days")


