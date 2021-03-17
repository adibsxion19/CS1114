# Aadiba Haque
# CS - UY 1114
# 27 March 2020
#Lab 8 Problem 3

def has_punctuation(s):
    # sig: str --> bool
    punctuation = False
    for ch in s:
        if ch in "'.,;:?!":
            punctuation = True
    p = print(punctuation)
    return p

print(has_punctuation(4))



    
        
            
        
            