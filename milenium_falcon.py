from time import sleep
import os

falcon_ascii = """
                       ____               /._\                                 
                       \__<---____________X__/                                 
                   .-^"~___~Z"^-._`'_____ ___~-.______                         
      ___,.---==='~[~~7^___^\"-._ 7~_____H__||"-. \__.^~""~"-------...,__      
  .--^---+-----------Y /\_/\ Y--^Y [_____H__||   ^._______/"~~~~"^------^---,- 
  |______|___________l [/ \] !___l       H  "^----z^------^----------------{   
   "~^----....________\^---^/_____\      H    _.-~_____________,...---------^  
                      ~"---"~     ~"-----"---^~~~"
"""


x_wing = """
   =[________]========-------[]<--
     |  ___ |
     |==|  ||
     |==| _| |
     |==||   |
     |  ||   |
     |  ||    |
     |  ~~    |
     |________|
   __L________\_
  <_|_L___/   | |,
     |__\_____|_|___
    /L___________   `---._________
   | | .----. _  |---v--.______ _ `-------------.--.__
  [| | |    |(_) |]__[_____]____________________]__ __]
   | |___________|---^--'_________.-------------`--'
    \L______________.---'
   __|__/_    | |
  <_|_L___\___|_|'
     L________/
     |        |
     |   _    |
     |  ||    |
     |  ||   |
     |==||_  |                                             
     |==|  | |                     
     |==|__||                                               
     |______|
   =[________]========-------[]<--                         
"""

def falcon_move(falcon_ascii, width):
    falcon_ascii_list = falcon_ascii.split('\n')
    result = []
    falcon_moved_list = [' ' + x for x in falcon_ascii_list]
    for line in falcon_moved_list:
        result.append(line[:width])
    return '\n'.join(result)


#falcon_move(falcon_ascii)


def falcon_fly(falcon_ascii=falcon_ascii):
    _, columns = os.popen('stty size', 'r').read().split()

    for _ in range(int(columns)):
        os.system('clear')
        print(falcon_ascii)
        falcon_ascii = falcon_move(falcon_ascii, int(columns))
        sleep(0.05)

if __name__ == '__main__':
    falcon_fly(x_wing)
