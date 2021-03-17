#Aadiba Haque
#4/24/2020
#Lab 12 Q3
def squared_numbers(filename, outFile):
    file = open(filename,"r")
    output = open(outFile,"w")
    for line in file:
        line = line.strip()
        if line == '':
            continue
        print(int(line)**2,file=output)
    file.close()
    output.close()

def main():
    filename = "numbers.txt"
    outFile = "num_squared.txt"
    squared_numbers(filename, outFile)
main()