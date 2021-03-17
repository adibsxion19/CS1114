# Author: Aadiba Haque
# Assignment / Part: HW3 - Q5
# Date due: 2020-02-28
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import math

print("Please enter lengths of a triangle's sides.")
# I rounded to 5 values after decimal places because then, two sides will be considered
#equal if they are not apart for more than 0.00001.

side_1 = round(float(input("Length of first side: ")),5)
side_2 = round(float(input("Length of second side: ")),5)
side_3 = round(float(input("Length of third side: ")),5)

hyp_side_3 = round(math.sqrt(math.pow(side_2, 2) + math.pow(side_1, 2)),5)
hyp_side_1 = round(math.sqrt(math.pow(side_2, 2) + math.pow(side_3, 2)),5)
hyp_side_2 = round(math.sqrt(math.pow(side_1, 2) + math.pow(side_3, 2)),5)

if side_1 == side_3 and side_2 == side_3:
    print(side_1,", ", side_2,", ", side_3, "form an equilateral triangle.")
    
elif side_1 == side_3 or side_2 == side_3 or side_1 == side_2:
    if side_1 == side_2 and side_3 == hyp_side_3:
        print(side_1,",", side_2,",", side_3, "form an isosceles right triangle.")     
    elif side_2 == side_3 and side_1 == hyp_side_1:
        print(side_1,", ", side_2,",", side_3, "form an isosceles right triangle.")   
    elif side_1 == side_3 and side_2 == hyp_side_2:
        print(side_1,",", side_2,",", side_3, "form an isosceles right triangle.")
    else:
        print(side_1,",", side_2,",", side_3, "form an isosceles triangle that is not a right triangle.")
        
else:
    print(side_1,",", side_2,",", side_3, "form an scalene triangle.")
    
      

    
   

