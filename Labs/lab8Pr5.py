# Aadiba Haque
# CS - UY 1114
# 27 March 2020
#Lab 8 Problem 5

def calc(s):
    #sig: str --> int
    first_space = s.find(' ')
    last_space = s.rfind(' ')
    operand1 = int(s[:first_space])
    operator = s[first_space+1: last_space]
    operand2 = int(s[last_space +1:])
    if operator == '+':
        answer = operand1 + operand2
    elif operator == '-':
        answer = operand1 - operand2
    elif operator == '*':
        answer = operand1 * operand2
    print(answer)
    return answer
    
