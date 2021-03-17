
class Character:
    def __init__(self,name,type_char,Attack,Defense,HP,SP):
        self.stats = {"Attack":Attack,"Defense":Defense,"HP": HP,"SP":SP}
        self.name = self.name
        self.type = self.type_char
    def __str__(self):
        return "{} ({}):\n{}:{}\n{}:{}\n{}:{}\n{}:{}\n".format(name,type,"Attack",stats["Attack"], "Defense",stats["Defense"],"HP",stats["HP"],stats["SP"])
class Party:
    def __init__(self,filename):
        lst = []
        file = open(filename,"r")
        file.readline()
        for lines in file:
            lines= lines.strip()
            lst_data = lines.split(",")
            lst.append(lst_data)
        self.members = lst
        file.close()              
    def __str__():
        for elem in self.members:
            string = elem + '\n'
        return string
def main():
    someCharacter = Character("Mario", "Plumber", "100","60", "200", "150")
    print(someCharacter.name)
    print(someCharacter.type)
    print(someCharacter.stats["Attack"])
    print(someCharacter.stats["Defense"])
    print(someCharacter.stats["HP"])
    print(someCharacter.stats["SP"])   ​
    print() # a new line for clarity
    ​
    print(someCharacter)
    party = Party("saveData.csv") 
    # this file address may be different for you
    ​
    print("PRINTING ONE MEMBER ONLY:")
    print(party.members[0])
    print()
    ​
    print("PRINTING WHOLE PARTY:")
    print(party)
        
