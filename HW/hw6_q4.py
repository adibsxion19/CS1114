# Author: Aadiba Haque
# Assignment / Part: HW6 - Q4
# Date due: 2020-04-03
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

def number_of_words(sentence):
    #sig: str --> int
    num_words= 0
    prev_char = ''
    for char in sentence:
        if (prev_char == ' ' or (prev_char in "'.,;:?!")) and char.isalnum():
            num_words += 1
        prev_char = char
    return num_words

def main():
    sentence = input("Please enter a sentence: ")
    print("There are", number_of_words(sentence), "words in your sentence.")

main()

