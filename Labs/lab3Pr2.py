# Aadiba Haque
# CS - UY 1114
# 14 February 2020
#Lab 3 Problem 2

import random
x = chr(random.randint(97, 122))
y = chr(random.randint(97, 122))
z = chr(random.randint(97, 122))
abc = x+y+z
cab = z+x+y
bca = y+z+x

print(abc)
print(cab, abc > cab)
print(bca, abc > bca)


