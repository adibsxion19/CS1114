# Aadiba Haque
# CS - UY 1114
# 3 March 2020
#Lab 9 Q4

#(1)
def printed_shifted_triangle(n,m,symbol):
    #sog: int, int, str ---> str
    #n=lines m=spaces
    num_symbol = 1
    for row in range(1, n+1):
        print((' '* m) + (' ' *(n - row)), end = '')
        print(symbol * num_symbol)
        num_symbol += 2
#(2) 
def print_pine_tree(n, symbol):
    #sig:int, str --> str
    #n = # of triangles
    num_lines = 2
    for space in range(n-1, -1, -1):
        printed_shifted_triangle(num_lines,space, symbol)
        num_lines += 1


def main():
    n = int(input("Number of triangles: "))
    symbol = input("Symbol: ")
    print_pine_tree(n, symbol)
main()


