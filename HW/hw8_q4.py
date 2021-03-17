# Author: Aadiba Haque
# Assignment / Part: HW8 - Q4
# Date due: 2020-04-24
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.
def clean_data(complete_data_filename, cleaned_data_filename):
    #sig: string, string
    complete_data = open(complete_data_filename,"r")
    cleaned_data = open(cleaned_data_filename,"w")
    output = ''
    lst_of_indices = (2,3,4,7,8,9)
    for lines in complete_data:
        lines = lines.strip()
        lst_values = lines.split(',')
        for index in lst_of_indices:
            output += lst_values[index] + ','
        output = output.strip(',')
        output += '\n'
    print(output, file=cleaned_data)
    complete_data.close()
    cleaned_data.close()
    
def convert_date_time_to_edt(cleaned_data_filename, edt_file_name):
    #sig: string, string
    #UTC is 4 hours ahead of EDT
    cleaned_data = open(cleaned_data_filename,"r")
    edt_file = open(edt_file_name,"w")
    counter = 0    
    output = ''
    lst_of_indices = (1,0,2,3,4,5)
    for lines in cleaned_data:
        lines = lines.strip()
        if lines == '':
            continue
        lst_values = lines.split(',')
        if counter == 0:
            temp = lst_values[1]
            lst_values[1] = lst_values[0]
            lst_values[0] = temp
            lst_values[2] = "Last Update Date"
            lst_values.insert(3,"Last Update Time (EDT)")
            output += ','.join(lst_values)
        else:
            for index in lst_of_indices:
                if index == 2:
                    last_update = lst_values[2].split()
                    date = last_update[0]
                    time = last_update[1].split(':')     
                    if int(time[0]) < 4:
                        date_lst = date.split('/')
                        date_lst[1] = str(int(date_lst[1])- 1)
                        output += '/'.join(date_lst) + ','
                    else:
                        output += date + ','
                    last_update_time = int(time[0]) - 4
                    if last_update_time < 0:
                        last_update_time += 24
                    time[0] = str(last_update_time)
                    output += ':'.join(time) + ','
                else:
                    output += lst_values[index] + ','
        counter += 1
        output = output.strip(',')
        output += '\n'
    print(output, file=edt_file)
    cleaned_data.close()
    edt_file.close()
    
def print_percentages_per_location(location, data_filename, type):
    data = open(data_filename,"r")
    header = True
    for lines in data:
        if header:
            header = False
            continue
        else:
            lines = lines.strip()
            if lines == '':
                continue
            lst_values = lines.split(',')
            if lst_values[1] == location:
                confirmed_cases = int(lst_values[4])
                num_types = 0
                if type == "death":
                    num_types = int(lst_values[5])
                elif type == "recovered":
                    num_types = int(lst_values[6]) 
                if num_types >= confirmed_cases:
                    print("There were {} {} of {} confirmed cases, or approximately 100.000%".format(num_types,type,confirmed_cases))
                else:
                    percent = num_types/confirmed_cases
                    print("There were {} {} of {} confirmed cases, or approximately {:.3%}".format(num_types,type,confirmed_cases,percent))
    data.close()
    
def difference_in_cases(location1, location2,edt_file_name):
    #location1 and location2 are the names of two states/provinces
    #edt_file_name is the name of the input file
    #This function prints the number of confirmed cases for each location1 and location2 and prints
    #to the screen the difference (absolute value) between the number of confirmed cases in location1 and location2
    #number of confirmed cases selected for each location is the first non-zero occurence found in the input file
    #if there are no non-zero occurences or the location is not found, the value of 0 is used as the number of cases for each location
    import math
    data = open(edt_file_name,"r")
    location1_cases = 0  
    location2_cases = 0  
    header = True 
    for lines in data:
        if header: 
            header = False 
            continue #so header is not counted in this function
        else: 
            lines = lines.strip() 
            if lines == '':     #accounts for the last line, if it is blank
                continue 
            lst_values = lines.split(',')
            if lst_values[1] == location1 and location1_cases == 0:
                location1_cases = int(lst_values[4])
            elif lst_values[1] == location2 and location2_cases == 0:
                location2_cases = int(lst_values[4])
            if location1_cases != 0 and location2_cases != 0:
                break
    difference = int(math.fabs(location1_cases - location2_cases))
    print("{}'s confirmed cases: {} \n{}'s confirmed cases: {} \nDifference: {}".format(location1,location1_cases,location2,location2_cases,difference))
    data.close()
    
def main():
    complete_data_filename = "03-25-2020.csv"
    cleaned_data_filename = "CleanedCovidData.csv"
    clean_data(complete_data_filename, cleaned_data_filename)
    edt_file_name = "NewCovidData.csv"
    convert_date_time_to_edt(cleaned_data_filename, edt_file_name)
    location = "New York"
    type = 'recovered'
    print_percentages_per_location(location, edt_file_name, type)
    print("What two states'/provinces' number of confirmed cases would you like to compare? ") #asking user names of states to compare their number of confirmed cases
    location1 = input() #name of first state assigned to variable location1
    location2 = input() #name of first state assigned to variable location2
    difference_in_cases(location1, location2,edt_file_name) #Calls the function and gives the difference between the number of confirmed cases for location1 and location2
main()
    