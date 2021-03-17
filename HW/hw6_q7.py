# Author: Aadiba Haque
# Assignment / Part: HW6 - Q7
# Date due: 2020-04-03
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.
def input_is_invalid(date_and_time): 
    #sig: str --> bool
    if len(date_and_time) != 19:
        return False
    month = date_and_time[:2]
    date = date_and_time[3:5]
    year = date_and_time[6:10]
    hour = date_and_time[11:13]
    minute = date_and_time[14:16]
    second = date_and_time[17:]
    if month.isdigit() and date.isdigit() and year.isdigit():   
        if int(month) > 12 or int(month) == 0 or int(year) == 0:
            return False
        if month == '01' or month== '03' or month == '05' or month == '07' or month == '08' or month =='10' or month == '12':
            if not (0 < int(date) <= 31):
                return False
        elif month == '04' or month == '06' or month =='09' or month == '11':
            if not (0 < int(date) <= 30):
                return False
        elif month == '02':
            if not(0 < int(date) <= 28): 
                return False
    else:
        return False
    if not(date_and_time[2] == '/' and date_and_time[5] == '/' and date_and_time[10] == ' ' and date_and_time[-6] ==':' and date_and_time[-3] ==':'):
        return False
    if hour.isdigit() and minute.isdigit() and second.isdigit():
        if int(hour) >= 24:
            return False
        if int(minute) >= 60:
            return False
        if int(second) >= 60:
            return False       
    else:
        return False
    return True
def date_time_parser(date_and_time):
    #sig: str
    if input_is_invalid(date_and_time) == True:
        month = date_and_time[:2]
        date = date_and_time[3:5]
        year = date_and_time[6:10]
        hour = int(date_and_time[11:13])
        minute = int(date_and_time[14:16])
        second = int(date_and_time[17:])
        print(date +'/'+ month +'/'+year[2:])
        if hour == 12:
            print (str(hour).zfill(2)+":"+str(minute).zfill(2)+":"+str(second).zfill(2))
            am_or_pm = "PM"
        elif hour == 0:
            hour = 12
            print(str(hour).zfill(2)+":"+str(minute).zfill(2)+":"+str(second).zfill(2))
            am_or_pm = "AM"
        elif hour > 12:
            hour -= 12
            print (str(hour).zfill(2)+":"+str(minute).zfill(2)+":"+str(second).zfill(2))
            am_or_pm = 'PM'
        elif hour < 12:
            print(str(hour).zfill(2)+":"+str(minute).zfill(2)+":"+str(second).zfill(2))
            am_or_pm = 'AM'
        print(month+'/'+year)
        print(am_or_pm)

def main():
    date_and_time = input("Please enter the date and time (24-hour clock) in 'MM/DD/YYYY HR:MIN:SEC' format: ")
    if input_is_invalid(date_and_time) == False:
        print("Invalid Input")
    else:
        print("Valid Input")
    date_time_parser(date_and_time)
main()