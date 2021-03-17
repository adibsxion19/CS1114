#Aadiba Haque
#Lab 13 Problem 3
#May 1 2020
class HeapOfBeans:
    def __init__(self):
        self.beans = 16
    def is_over(self):
        if self.beans == 0:
            return True
        return False
    def player_1_turn(self):
        import random
        remove_beans = random.randint(1,3)
        if remove_beans > self.beans:
            remove_beans = self.beans
            self.beans = 0
        else:
            self.beans -= remove_beans
        print("player 1 removed {} beans, {}  beans remaining.".format(remove_beans,self.beans))
    def player_2_turn(self):
        import random
        remove_beans = random.randint(1,3)
        if remove_beans > self.beans:
            remove_beans = self.beans
            self.beans = 0
        else:
            self.beans -= remove_beans
        print("player 2 removed {} beans, {}  beans remaining.".format(remove_beans,self.beans))
def main():
    game = HeapOfBeans()
    while not game.is_over():
        game.player_1_turn()
        if game.is_over():
            print("Player 1 lost")
            break
        game.player_2_turn()
        if game.is_over():
            print("Player 2 lost")
main()
    
#        if beans <= 0:
#            print("Player 1 lost")
#        beans = class_call.player_2_turn()
#        if beans <= 0:
#            print("Player 2 lost")
      