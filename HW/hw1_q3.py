# Author: Aadiba Haque
# Assignment / Part: HW1 - Q3
# Date due: 2020-02-14
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

print("Please enter number of coins:")
quarter = int(input("Quarters:"))
dime = int(input("Dimes:"))
nickel = int(input("Nickels:"))
penny = int(input("Pennies:"))

total_money = (quarter*25) + (dime*10) + (nickel*5)+ (penny)

dollars = total_money // 100
cents = total_money % 100
print("The total is", dollars, "dollars and", cents, "cents.")
