# class Appt:
#     def __init__(self, title, start, duration):
#         self.title = title
#         self.start = start
#         self.end = start + duration
#         self.members = []
#         
#     def __repr__(self):
#         return "Start Time: " + self.title + " start time: "+ str(self.start)
#     + " end time: " + str(self.end)
#     
#     def add_participant(self, email):
#         self.members.append(email)
#         message = "Start Time: " + self.title + " start time: "+ str(self.start)
#     + " end time: " + str(self.end)
#         send_email(email, message)
#         
#     def __str__(self):
#         return "Start Time: " + self.title + " start time: "+ str(self.start)
#     + " end time: " + str(self.end)
    
# class FuelTank():
#     def __init__(self,capacity=10):
#         self.gallons = 0.0
#         self.capacity = capacity
#     def __str__(self):
#         return "Gallons:{} \n Capacity:{}".format(self.gallons,self.capacity)
#     def fill(self,gallons_in):
#         if self.capacity >= gallons_in +self.gallons:
#             self.gallons += gallons_in
#         else:
#             self.gallons = self.capacity
#     def is_empty(self):
#         if self.gallons == 0:
#             return True
#         else:
#             return False
#     def get_percent_full(self):
#         return (self.gallons / self.capacity)*100
#     def use_fuel(self,rate_per_hour,hours):
#         if rate_per_hour*hours > self.gallons:
#             self.gallons = 0
#             raise ValueError("Not enough Fuel!")
#         else:
#             self.gallons -= rate_per_hour*hours
# def main():
#     tank1 = FuelTank(10)
#     print(tank1.is_empty()) #True
#     tank1.fill(7)
#     print(tank1.get_percent_full()) #70.0
#     tank1.fill(12)
#     print(tank1.get_percent_full()) #100.0
#     tank1.use_fuel(0.5, 21) #ValueError Not Enough Fuel!
# main()
class Money():
    def __init__(self, dollars=0,cents=0):
        self.dollars = dollars
        if cents > 100:
            self.dollars += cents // 100
        self.cents = cents % 100
    def __str__(self):
        return "${}.{}".format(self.dollars,str(self.cents).zfill(2))
    def __add__(self,other):
        newDollars = self.dollars + other.dollars
        newCents = self.cents + other.cents
        return Money(newDollars, newCents)
    def __lt__(self,other):
        if self.dollars > other.dollars:
            return False
        elif self.dollars == other.dollars:
            if self.cents > other.cents:
                return False
            else:
                return True
        else:
            return True
def main():
    money1 = Money(1,102)
    money2 = Money(2,20)
    print(money1)
    print(money2)
    print(money1 + money2)
    print(money1 < money2)

main()






























