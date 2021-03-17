#Aadiba Haque
#4/24/2020
#Lab 12 Q5
def add_entry(contacts, name, number):
    if name not in contacts:
        if len(number) == 10:
            valid = True
            for num in number:
                if not num.isdigit():
                    valid = False
            if valid:
                contacts[name] = number
def lookup(contacts, name):
    if name in contacts:
        return contact[name]
    else:
        print("Name not found")
def print_all(contacts):
    for key in contacts:
        print(key, contacts[key],sep = '\t')
def add_from_file(filename, contacts):
    try:
        file = open(filename, "r")
    except:
        print("File Not Found")
    for line in file:
        line = line.strip()
        lst_data = line.split(",")
        name = lst_data[0]
        name_lst = name.split(", ")
        temp = name_lst[0]
        name_lst[0] = name_lst[1]
        name_lst[1] = temp
        name = " ".join(name_lst)
        add_entry(contacts, name, lst_data[1])
    file.close()
def main():
    contacts = {}
    filename = "us-senate.csv"
    name = "Mickey Mouse"
    number = "1234567890"
    add_from_file(filename, contacts)
    add_entry(contacts, name, number)
    lookup(contacts, name)
    print_all(contacts)
    
