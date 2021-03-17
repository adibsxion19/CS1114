# print("  *")
# print(" * *")
# print("*   *") 
# print("*****")
# print("*   *")
# print("*   *")
# print("     ")
# print("*   *")
# print("*   *")
# print("*   *")
# print("*****")
# print("*   *")
# print("*   *")

# print("Enter the hours worked: ")
# hours_total = 0
# days = 0
# overtime_days = 0
# hours_input = 0
# payRate = 10
# 
# while hours_input >= 0:
#     hours_input = int(input())
#     hours_total += hours_input
#     days += 1
#     if hours_input > 10:
#         overtime_days += 1
#        
# if hours_total > 40:
#     overwork = hours_total - 40
#     reg_hours = hours_total - overwork
#     bonus_pay = 13*overtime_days
#     overtime_pay = 1.5*overwork*payRate
#     reg_pay = reg_hours * payRate
# print("Bonus Pay: $", bonus_pay)
# print("Overtime Pay: $", overtime_pay)
# print("Total Pay: $", bonus_pay + overtime_pay +reg_pay)


print("Enter the hours worked: ")
hours_input = 0
hours_total = 0
overtime_days = 0
payRate =  10

while hours_input >= 0:
    hours_total += hours_input
    if hours_input > 10:
        overtime_days += 1
    hours_input = int(input())
    
if hours_total > 40:
    overwork = hours_total - 40
    reg_hours = hours_total - overwork
    bonus_pay = 13*overtime_days
    overtime_pay = 1.5*overwork*payRate
    reg_pay = reg_hours * payRate

else:
    overwork = 0
    reg_hours = hours_total - overwork
    bonus_pay = 13*overtime_days
    reg_pay = reg_hours * payRate
    overtime_pay = 0

print("Bonus Pay: $", bonus_pay)
print("Overtime Pay: $", overtime_pay)
print("Total Pay: $", bonus_pay + overtime_pay + reg_pay)

