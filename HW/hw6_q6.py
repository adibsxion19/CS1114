# Author: Aadiba Haque
# Assignment / Part: HW6 - Q6
# Date due: 2020-04-03
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

def yards_to_miles(yards):
    #sig: float --> float
    miles = yards / 1760
    return miles
def main():
    yards = float(input("What is the measurement in yards?"))
    print("The number of miles:", yards_to_miles(yards))
main()
    
