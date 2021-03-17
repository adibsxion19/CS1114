# Aadiba Haque
# CS - UY 1114
# 3 March 2020
#Lab 9 Q5

def find(some_string, substring, start, end):
    #start <= index < end
    #sig: str, str, int, int --> int
    #substring = CG and ATCGCGAT return 2
    #substring length would be 2 and we find C at indexx 2
    #string index = 2 and string_index+substrig length = 4
    #we are checking if some_string[2:4] == CG
    substr_len = len(substring)
    for string_index in range(start,end):
        if substring[0] == some_string[string_index]:
            if substring == some_string[string_index:string_index + substr_len]:
                return string_index
    return -1
def main():
    some_string = input("What is the string: ")
    substring= input("What is the substring: ")
    start,end = int(input("Start:")),int(input("End:"))
    #end = int(input("End: "))
    print(find(some_string, substring, start, end))
    
main()