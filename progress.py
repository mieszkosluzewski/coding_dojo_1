"""
  ________
  |      |
  O      |
 /|\     |
 / \     |
         |
 GAME OVER!
"""


def progress(letters_count):
    """
    Return progress in hangman for letters_count.
    For letters_count < 0  return empty gallows.
    For letters_count >= 6 return full picture with Game Over message.


    :param int: letters_count: Number of used letters

    :rtype: str
    :return: ASCII art with progress in hangman.
    """

    gallow = [list(line) for line in [
        '  ________',
        '  |      |',
        '  O      |',
        ' /|\     |',
        ' / \     |',
        '         |',
    ]]
    indexes = (
        (2, 2),
        (3, 1),
        (3, 2),
        (3, 3),
        (4, 1),
        (4, 3),
    )
    if letters_count >= 6:
        return '\n'.join([''.join(line) for line in gallow] + ['GAME OVER!'])
    for x, y in indexes[letters_count:]:
        gallow[x][y] = ' '

    return '\n'.join([''.join(line) for line in gallow] + ['          '])