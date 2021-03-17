# Author: Aadiba Haque
# Assignment / Part: HW6 - Q5
# Date due: 2020-04-03
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.
import math
def approximate_pi(num_terms):
    #int --> float
    power = 0
    multiply_by = 1
    summation = 0
    counter = 1
    while counter <= num_terms:
        if counter % 2 == 0:
            summation -= (1/(multiply_by * math.pow(3,power)))
        else:
            summation += (1/(multiply_by * math.pow(3,power)))
        pi = math.sqrt(12) * (summation)
        multiply_by = multiply_by + 2
        power += 1
        counter += 1
    return pi
       
def main():
    num_terms = int(input("Please enter number of terms you want to approximate pi to: "))
    print("Pi is approxiametly", approximate_pi(num_terms))

main()