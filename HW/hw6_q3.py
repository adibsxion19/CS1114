# Author: Aadiba Haque
# Assignment / Part: HW6 - Q3
# Date due: 2020-04-03
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

def largest_of_three(value1, value2, value3):
    # sig: float or int, float or int, float or int --> float or int
    if value1 >= value2 and value1 >= value3:
        return value1
    elif value2 >= value1 and value2 >= value3:
        return value2
    elif value3 >= value1 and value3 >= value2:
        return value3

def main():
   print("Please input 3 values:")
   value1 = input()
   value2 = input()
   value3 = input()
   if '.' in value1:
       value1 = float(value1)
   else:
       value1 = int(value1)
   if '.' in value2:
       value2 = float(value2)
   else:
       value2 = int(value2)
   if '.' in value3:
       value3 = float(value3)
   else:
       value3 = int(value3)
   print("The largest value is:", largest_of_three(value1, value2, value3))
   
main()
    
