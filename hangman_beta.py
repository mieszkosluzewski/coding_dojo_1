import os

from secret_words import words
from random import shuffle
from string import ascii_lowercase
from progress import progress


def word():
    """Losuje słowo."""
    shuffle(words)
    return words[0]


def data():
    """Pobiera litere od użytkownika."""
    while True:
        letter = input("Podaj literę: ")
        if len(letter) >1:
            print ("Błąd. Proszę podać jedną literę")
        elif letter not in ascii_lowercase:
            print("Błąd. Mogą być tylko małe litery")
        else:
            break
    return letter

def add_list(word, letters):
    """
    Zwraca częściowo wypełnione słowo dla utkownika.

    Np. dla słowa 'sokół milenium' i liter ['s', 'o']

    so*** ********

    :param str word: zgadywane słowo

    :rtype: str
    :return: wypełnione słowo
    """
    display =''
    for ltr in word:
        if ltr in letters:
            display += ltr
        elif ltr == ' ':
            display += ' '
        else:
            display += '*'

    return display



def main_loop():
    os.system("clear")
    used_letters = []
    guessd_word = word()
    print(progress(0))
    print(add_list(guessd_word, used_letters))

    used_letters.append(data())

    while True:
        os.system("clear")
        bad_letters = [letter for letter in used_letters if letter not in guessd_word]
        print(progress(len(bad_letters)))
        hidden = add_list(guessd_word, used_letters)
        print(hidden)
        print(used_letters)
        if guessd_word == hidden:
            os.system("sl -F")
            break
        if len(bad_letters) == 6:
            print(guessd_word)
            break
        used_letters.append(data())

main_loop()