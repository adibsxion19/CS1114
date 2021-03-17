# Aadiba Haque
# CS - UY 1114
# 17 April 2020
#Lab 11 Question 6
def ht1(hashtag):
    #sig: string --> list(strings)
    phrase = ''
    for ch in hashtag:
        if ch.isupper():
            phrase += ' '
        if ch.isalpha():
            phrase += ch.lower()
    list_of_words = phrase.split()
    return list_of_words
print(ht1("#midtermsAreCool"))
print(ht1("#SpatulaKing"))

        