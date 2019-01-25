# encoding utf-8

import os

alphabet = "azertyuiopqsdfghjklmwxcvbnéàçàâôöêë"


def empty_dictionnary():
    """ Creates an empty dictionnary, no argument"""
    dictionnary = {}

    for i in alphabet :
        dictionnary[i] = 0

    return dictionnary

def create_dictionnary(text):
    """ Creates a dictionnary to stock lettres and their number of occurences, takes a text in argument"""

    dictionnary = empty_dictionnary()
    
    for line in text :
        for letter in line :
            if letter in alphabet :
                dictionnary[letter]+=1 

    return dictionnary


def sum_letters(dictionnary):
    """Sums the total number of letters in a text file, takes a dictionnary associating each letter with their number of occurences in argument"""

    return sum(dictionnary[letter] for letter in alphabet)


def frequency(text):
    """Computes the frequency of each letters in a text file, takes a text in argument"""

    freq = empty_dictionnary()
    dictionnary = create_dictionnary(text)
    s = sum_letters(dictionnary)

    if s != 0 :
        for i in alphabet :
            freq[i] = dictionnary[i]/s
    
    return freq

def distance(dictionnary1, dictionnary2):
    """Computes the distance between the frequencies of each letters in a test file and a learning file, takes two dictionnaries associating each letter with their 
    frequences in argument"""

    dist = 0

    for i in alphabet :
        dist += abs(dictionnary1[i] - dictionnary2[i])

    return dist 


def save(dictionnary, file):
    """"Saves a file with the elements stocked in the dictionnary takes a file and a dictionnary associating each letter with their frequences in argument"""
    f = open(file, "w+")

    for letter in alphabet:
        f.write(letter + ":" + str(dictionnary[letter]) + "\n")

    f.close()


def load(file):
    """loads a file and fills a dictionnary with its elements, takes a file for its argument"""

    freq = empty_dictionnary()

    f = open(file, "r")

    for line in f:
        l = line.split(":")
        freq[l[0]]=int(l[1])
    
    f.close()

    return freq

def compare(text):
    """Compares the distances between the test text and the french training text and between the test text and the english training text
    returns minimum distance and thus gives the language of the test text""" 

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