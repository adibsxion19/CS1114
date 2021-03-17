# Author: Aadiba Haque
# Assignment / Part: HW9 - Q2
# Date due: 2020-05-01
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.
def find_stops_from_file(train_line):
    subway_stations = open("stations.csv","r")
    lst_of_stops = []
    for lines in subway_stations:
        lines = lines.strip('\n') 
        lst_of_data = lines.split(',')
        if (train_line in lst_of_data[7]):
            lst_of_stops.append(lst_of_data[5])
    subway_stations.close()
    return lst_of_stops

def make_dict(train_line,train_stops):
    train_stops_dict = {}
    for stops in train_stops:
        if train_line in train_stops_dict:
            if stops == train_stops[-1]:
                train_stops_dict[train_line] += stops
            else:
                train_stops_dict[train_line] += stops + ', '
        else:
            train_stops_dict[train_line] = stops + ', '
    return train_stops_dict

def format_dict(train_stops_dict):
    for key, value in train_stops_dict.items():
        output = "{} line: {}".format(key, value)
    return output

def main():
    train_line = input("Please enter a train line, or 'done' to stop: ")
    while train_line != 'done':
        print(format_dict(make_dict(train_line,find_stops_from_file(train_line))))
        train_line = input("Please enter a train line, or 'done' to stop: ")
main()
