# Author: Aadiba Haque
# Assignment / Part: HW1 - Q2 
# Date due: 2020-02-14
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.


current_pop = 330109174
year = int(input("How many years have passed? "))


birth = ((7*3600)*24)*365
death = ((13*3600)*24)*365
immigrants = ((35*3600)*24)*365

net_gain = birth - death + immigrants

new_pop = current_pop + (year * net_gain)

print("The estimated population for",str(year),"is:",new_pop)