# Author: Aadiba Haque
# Assignment / Part: HW6 - Q8
# Date due: 2020-04-03
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

def toPirate(en_sentence):
    word = ''
    prev_char = ' '
    pirate_sent = ''
    index = 0
    for char in en_sentence:
        if char.isalnum():
            word += char 
            continue
        new_word = ""
        if word.lower() == 'hello':
            new_word = 'avast'
        elif word.lower() == 'excuse':
            new_word = 'arrr'
        elif word.lower() == 'sir' or word == 'boy' or word == 'man':
            new_word = 'matey'
        elif word.lower() == 'madam':
            new_word = 'proud beauty'
        elif word.lower() == 'officer':
            new_word = 'foul blaggard'
        elif word.lower() == 'the':
            new_word = "th'"
        elif word.lower() == 'my':
            new_word =  'me'
        elif word.lower() == 'your':
            new_word = 'yer'
        elif word.lower() == 'is':
            new_word ='be'
        elif word.lower() == 'are': 
            new_word =  'be'
        elif word.lower() == 'restroom':
            new_word = 'head'
        elif word.lower() == 'restaurant':
            new_word =  'galley'
        elif word.lower() == 'hotel':
            new_word = 'fleabag inn'
        else:
            new_word = word
        word
        pirate_sent += new_word + char
        word = ''
    pirate_sent = pirate_sent[0].upper() + pirate_sent[1:]
    return pirate_sent

def main():
    en_sentence = input("Please input a English sentence: ")
    print("The translation to Pirate language is:", toPirate(en_sentence + " "))
    
main()