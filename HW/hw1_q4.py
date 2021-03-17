# Author: Aadiba Haque
# Assignment / Part: HW1 - Q4
# Date due: 2020-02-14
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

print("Please enter your amount in the format of dollars and cents in the two separate lines.")
dollars = int(input())
cents = int(input())
money = (dollars*100) + cents

quarter = money // 25
dime = (money - (25* quarter)) // 10
nickel = (money - ((25*quarter)+(10*dime))) // 5
penny = money - ((25*quarter)+(10*dime)+(5*nickel))

print(dollars,"dollars and",cents, "cents are:", quarter,"quarters,",dime,"dimes,",nickel, \
      "nickels,", "and", penny, "pennies.")

            
            