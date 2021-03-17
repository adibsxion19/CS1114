# Author: Aadiba Haque
# Assignment / Part: HW3 - Q3
# Date due: 2020-02-28
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

day = input("Enter the day the call started at: ")
time = int(input("Enter the time the call started at (hhmm): "))
duration = int(input("Enter the duration of the call (in minutes): "))
 


if  day == "Mon" or day == "Tue" or day == "Wed" or day =="Thr" or day =="Fri":
    if 800 <= time and time <= 1800:
        duration *= 0.40
    elif 800 > time or time > 1800: 
        duration *= 0.25
    
if day == "Sat" or day == "Sun":
    duration *= 0.15

print()
print("This call will cost $"+str(duration))
