Zadanie 1:

Napisać grę "Hangman".
W pliku secret words znajduje się lista słów, które posłużą do zgadywania.

Program powinien wyświetlać aktualny stan szubienicy (gotowa funkcja)
oraz odkryte literki zgadywanego słowa. Ponadto dobrze, jakby wyświetlał wcześniej zgadywane literki.

Uwzględnić błędne dane użytkownika.

Zadanie 2:

Przerobić powyższy program na webservice napisany we Flasku.



HINTS:

Czyszczenie terminala:

import os

os.system("clear")  # Działa pod linuxem. Pod Windowsem os.system("cls")


ASCII art w przeglądarce (umieszczenie kodu w znacznikach <pre></pre> nie wyrzuci nam spacji
(domyślne zachowanie html'a)

Przydatna może też być czcionka typu monospaced:
np. Courier New