# Aadiba Haque
# CS - UY 1114
# 3 March 2020
#Lab 9 Q2

def digit1(string):
    #sig: str
    even_num = ''
    odd_num = ''
    for char in string:
        if char== '0' or char == '2' or char =='4' or char == '6' or char =='8':
            even_num += char
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            odd_num += char
    return len(even_num), len(odd_num)
def digit2(string):
    even_count = 0
    odd_count = 0
    num = int(string)
    #temp_num = num
    while num > 0:
        digit = num % 10
        num //= 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

def main():
    string = input("Please input a string: ")
    even_count, odd_count = digit1(string)
    print("Even digits:", even_count, "Odd digits:", odd_count)
    even_count, odd_count = digit2(string)
    print("Even digits:", even_count, "Odd digits:", odd_count)
main()
    

        