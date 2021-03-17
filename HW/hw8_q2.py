# Author: Aadiba Haque
# Assignment / Part: HW8 - Q2
# Date due: 2020-04-24
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.
def write_thatFile(thisFile):
    string_output = ''
    counter = 0
    for lines in thisFile:
        if counter % 2 == 0:
            string_output += lines
        counter += 1
    return string_output
def main():
    thisFile = open("thisFile.txt", "r")
    thatFile = open("thatFile.txt", "w")
    print(write_thatFile(thisFile), file=thatFile)
    thisFile.close()
    thatFile.close()
main()
