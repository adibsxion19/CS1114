# Author: Aadiba Haque
# Assignment / Part: HW5 - Q7 Part A
# Date due: 2020-03-13
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic

Roman_number = input("Enter number in the simplified Roman system: ")
total = 0
for every_digit in Roman_number:
    if every_digit == 'I':
        total += 1
    elif every_digit == 'V':
        total += 5
    elif every_digit == 'X':
        total += 10
    elif every_digit == 'L':
        total += 50
    elif every_digit == 'C':
        total += 100
    elif every_digit == 'D':
        total += 500
    elif every_digit == 'M':
        total += 1000
print(Roman_number, 'is', total)

        