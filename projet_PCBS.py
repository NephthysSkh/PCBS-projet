# encoding utf-8

import os

alphabet = "azertyuiopqsdfghjklmwxcvbnéàçàâôöêë"


def empty_dictionnary():
    dictionnary = {}

    for i in alphabet :
        dictionnary[i] = 0

    return dictionnary

def create_dictionnary(text):
    """ """
    dictionnary = empty_dictionnary()
    
    for line in text :
        for letter in line :
            if letter in alphabet :
                dictionnary[letter]+=1 

    return dictionnary


def sum_letters(dictionnary):

    return sum(dictionnary[letter] for letter in alphabet)


def frequency(text):
    freq = empty_dictionnary()
    dictionnary = create_dictionnary(text)
    s = sum_letters(dictionnary)

    if s != 0 :
        for i in alphabet :
            freq[i] = dictionnary[i]/s
    
    return freq

def distance(dictionnary1, dictionnary2):

    dist = 0

    for i in alphabet :
        dist += abs(dictionnary1[i] - dictionnary2[i])

    return dist 


def save(dictionnary, file):
    f = open(file, "w+")

    for letter in alphabet:
        f.write(letter + ":" + str(dictionnary[letter]) + "\n")

    f.close()


def load(file):
    freq = empty_dictionnary()

    f = open(file, "r")

    for line in f:
        l = line.split(":")
        freq[l[0]]=int(l[1])
    
    f.close()

    return freq

def compare(text):

    if os.path.isfile("./freq_FR.txt"):
        freq_FR = load("freq_FR.txt")
    else:
        freq_FR = frequency(open("alice_Fr.txt", "r").read().lower())
        save(freq_FR, "freq_FR.txt")

    if os.path.isfile("./freq_EN.txt"):
        freq_EN = load("freq_EN.txt")
    else:
        freq_EN = frequency(open("alice_En.txt", "r").read().lower())
        save(freq_EN, "freq_EN.txt")

    freq = frequency(text)

    if distance(freq_FR, freq) < distance(freq_EN, freq) :
        print("Le texte est en français")
    else:
        print("Le texte est en anglais")




text = open('test2.txt', 'r').read().lower()

compare(text)