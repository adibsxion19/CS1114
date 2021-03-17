#Aadiba Haque
#4/24/2020
#Lab 12 Q2

def consecutive_numbers(filename,n):
    #sig: str, int --> NoneType
    text_file = open(filename, "w")
    string = ''
    for consec_int in range(1,n+1):
        string += str(consec_int) + "\n"
    print(string, file=text_file)
    text_file.close()
def main():
    filename = "numbers.txt"
    consecutive_numbers(filename,5)
main()