# Author: Aadiba Haque
# Assignment / Part: HW8 - Q3
# Date due: 2020-04-24
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.
def process_file(inputFile):
    reverse_order = ''
    for lines in inputFile:
        lines = lines.strip('\n') 
        lst = lines.split()     
        for elem in lst:
            reverse_order += elem[::-1]
            reverse_order += ' '
        reverse_order += '\n'
    return reverse_order
def main():
    fileNotFound = True
    while fileNotFound:
        inputFile = input("Full name of input file: ")
        try:
            inputFile = open(inputFile, "r")
            fileNotFound = False
        except FileNotFoundError:
            print("Input file was not found.")
            fileNotFound = True
    print(process_file(inputFile))
    inputFile.close()
main()

