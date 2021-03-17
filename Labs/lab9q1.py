# Aadiba Haque
# CS - UY 1114
# 3 March 2020
#Lab 9 Q1

def calculation(variable1, variable2):
    #sig: int, int --> int, int
    addition = variable1 + variable2
    subtraction = variable1 - variable2
    return addition, subtraction

res1, res2 = calculation(40, 10)
print("res1 =",res1, "res2 =", res2)
