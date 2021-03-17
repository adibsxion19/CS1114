# Author: Aadiba Haque
# Assignment / Part: HW2 - Q5 
# Date due: 2020-02-21
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

John_days = int(input("Please enter the number of days John has worked: "))
John_hours = int(input("Please enter the number of hours John has worked: "))
John_minutes = int(input("Please enter the number of minutes John has worked: "))
Bill_days = int(input("Please enter the number of days Bill has worked: "))
Bill_hours = int(input("Please enter the number of hours Bill has worked: "))
Bill_minutes = int(input("Please enter the number of minutes Bill has worked: "))

total_days_to_minutes = ((John_days + Bill_days) * 24)* 60
total_hours_to_minutes = (John_hours + Bill_hours) * 60
total_minutes = John_minutes + Bill_minutes

total_time = total_days_to_minutes + total_hours_to_minutes + total_minutes

total_days = int((total_time / 60)/ 24)
total_hours = int(((total_time / 60) % 24))
total_minutes = int((((total_time / 60) % 24) % 1) *60)

print("The total time both of them worked together is: ", total_days, "days", total_hours, "hours and", total_minutes, "minutes.")



