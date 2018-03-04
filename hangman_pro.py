import os

from milenium_falcon import falcon_fly
from secret_words import words
from random import shuffle
from string import ascii_lowercase
from progress import progress


def get_word():
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

def make_board(hidden_word, letters):
    """
    Zwraca częściowo wypełnione słowo dla utkownika.

    Np. dla słowa 'sokół milenium' i liter ['s', 'o']

    so*** ********

    :param str hidden_word: zgadywane słowo

    :rtype: str
    :return: wypełnione słowo
    """
    display =''
    for ltr in hidden_word:
        if ltr in letters:
            display += ltr
        elif ltr == ' ':
            display += ' '
        else:
            display += '*'

    return display


def restart():
    while True:
        in_data = input('Czy chcesz zagrać ponownie [(T)ak/(N)ie]: ')
        if in_data.lower()[0] == 't':
            return True
        elif in_data.lower()[0] == 'n':
            return False
        else:
            print('Jeśli nie umiesz napisać Tak lub Nie, to godny nie jesteś w tę grę zagrać\n'
                  'młody Patafianie! Do przedszkola wróć nauki pobrać!')


def turn(guessed_word, used_letters):
    os.system("clear")
    bad_letters = [letter for letter in used_letters if letter not in guessed_word]
    print(progress(len(bad_letters)))
    hidden = make_board(guessed_word, used_letters)
    print(hidden)
    print(''.join(bad_letters))

    if guessed_word == hidden:
        #os.system("sl -F")
        falcon_fly()
        return True
    if len(bad_letters) == 6:
        print(guessed_word)
        return True
    used_letters.append(data())
    return False


def main_loop():
    used_letters = []
    guessed_word = get_word()
    while True:
        if turn(guessed_word, used_letters):
            if restart():
                used_letters = []
                guessed_word = get_word()
            else:
                break

main_loop()