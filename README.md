#Description du projet

Le projet avait pour but de construire un classifieur qui, à partir des fréquences d'apparition de chaque lettre dans un échantillon d'apprentissage en anglais et dans un échantillon d'apprentissage en français, permet de dire si un test test est en français ou en anglais. 

#Principe de fonctionnement

Le principe est de prendre un échantillon d'apprentissage assez grand en français et en anglais. J'ai utilisé pour les échantillons d'apprentissage le livre Alice au Pays des Merveilles (les fichiers alice_Fr et alice.En). J'ai quelques textes à tester de longueurs diverses (il s'agit des fichiers .txt). 

1. Dans un premier temps, on définit une fonction qui permet de créer un dictionnaire vide qui associe à chaque lettre de l'alphabet définit en variable globale la valeur 0, c'est la fonction empty_dictionnary, qui ne prend pas d'argument.

import os

alphabet = "azertyuiopqsdfghjklmwxcvbnéàçàâôöêë"

def empty_dictionnary():
    """ Creates an empty dictionnary, no argument"""
    dictionnary = {}

    for i in alphabet :
        dictionnary[i] = 0

    return dictionnary


2. Ensuite, on veut pouvoir remplir des dictionnaires qui associent à chaque lettre d'un texte leur nombre d'occurrence dans un texte donné. Pour ça, on définit la fonction create_dictionnary qui prend en argument le texte dans lequel on va compter le nombre d'occurrence de chaque lettre.

def create_dictionnary(text):
    """ Creates a dictionnary to stock lettres and their number of occurences, takes a text in argument"""

    dictionnary = empty_dictionnary()
    
    for line in text :
        for letter in line :
            if letter in alphabet :
                dictionnary[letter]+=1 

    return dictionnary


3. Pour pouvoir calculer les fréquences d'apparition de chaque lettre, on définit la fonction sum_letters qui compte le nombre total de lettres dans un texte donné et qui prend en argument le texte dont il faut compter les lettres. 


def sum_letters(dictionnary):
    """Sums the total number of letters in a text file, takes a dictionnary associating each letter with their number of occurences in argument"""

    return sum(dictionnary[letter] for letter in alphabet)


4. Maintenant on veut calculer les fréquences d'apparition de chaque lettres et les ranger dans un dictionnaire qui associe à chaque lettre sa fréquence d'apparition dans un texte donné. On définit donc la fonction frequency qui prend en argument le texte pour lequel il faut compter la fréquence d'apparition des lettres à l'aire des fonctions définies précédemment qui permettent de créer un dictionnaire vide qui associe à chaque lettre la valeur 0, puis qui compte pour chaque lettre dans le texte le nombre d'occurrence et enfin qui rapporte le nombre d'occurrence de chaque lettre au nombre total de lettres du texte pour donner la fréquence.

def frequency(text):
    """Computes the frequency of each letters in a text file, takes a text in argument"""

    freq = empty_dictionnary()
    dictionnary = create_dictionnary(text)
    s = sum_letters(dictionnary)

    if s != 0 :
        for i in alphabet :
            freq[i] = dictionnary[i]/s
    
    return freq



5. On définit une fonction compare qui prend en argument un texte que l'on veut tester pour en savoir la langue et qui crée pour ce texte un dictionnaire qui associe à chaque lettre de l'alphabet sa fréquence d'apparition, et calcule la distance entre les fréquences d'apparition de chaque lettre dans le texte test et les fréquences d'apparition de chaque lettre dans le texte d'apprentissage en français plus dans celui en anglais. Le texte test est dans la langue pour laquelle la distance est minimale.

def distance(dictionnary1, dictionnary2):
    """Computes the distance between the frequencies of each letters in a test file and a learning file, takes two dictionnaries associating each letter with their 
    frequences in argument"""

    dist = 0

    for i in alphabet :
        dist += abs(dictionnary1[i] - dictionnary2[i])

    return dist 

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



6. On ne veut pas avoir à recalculer les fréquences d'apparition de chaque lettre dans le texte d'apprentissage en français et en anglais à chaque fois qu'on teste un texte. On regarde donc dans compare si il y a un fichier en mémoire qui contient les fréquences d'apparition de chaque lettre du texte d'apprentissage. Si c'est le cas, on appelle la fonction load qui permet de l'ouvrir pour s'en servir. Si ce n'est pas le cas, on crée le fichier et on calcule les fréquences pour les y enregistrer. 


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


# Retour sur expérience
Je suis débutante en programmation. Je n'ai suivi auparavant que des cours très introductifs sur Python, sans avoir vraiment l'occasion de pratiquer. Je n'avais pas vraiment idée de ce qui pouvait être raisonnable de faire pour ce projet, j'ai donc pris une des idées de projet proposées puis au fur et à mesure de mon avancée, j'en ai simplifié le contenu pour qu'il corresponde mieux à mon niveau en programmation. 

Notamment, j'ai surtout essayé de créer autant de fonctions que possible, et de faire en sorte que chaque fonction ait une utilité précise, pour m'entraîner à découper chaque problème en sous-problèmes et les résoudre plus facilement. J'ai voulu ensuite utiliser des outils dont je comprenais bien le fonctionnement, j'ai donc testé plusieurs façons de faire, et l'utilisation des dictionnaires m'a paru le meilleur compromis entre la simplicité et la puissance de l'outil utilisé. Enfin, j'ai essayé raffiner mon programme en faisant en sorte de ne calculer qu'une fois les fréquences d'apparition de chaque lettre dans les textes d'apprentissage.

J'ai eu du mal à comprendre le fonctionnement de Git, et je pense que ça aurait pu être utile de faire plusieurs points dessus, même si ça peut être un peu répétitif. Notamment, je ne me suis rendue compte qu'au dernier moment qu'en fait je n'avais pas bien push mon rapport et mon programme sur le repository. Ensuite, certains cours magistraux étaient un peu trop rapides, comme par exemple ceux sur l'utilisation de numpy et de panda. Je n'ai pas pu tout suivre, et je me rends compte que ce sont des outils que j'aurais pu utiliser ici.