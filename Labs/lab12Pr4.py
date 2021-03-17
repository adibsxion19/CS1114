#Aadiba Haque
#4/24/2020
#Lab 12 Q4
def count_digits(lst):
    count = {}
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return count
def main():
    print(count_digits([1,2,3]))
    print(count_digits([2,0,1,9,0,4,1,9]))
main()