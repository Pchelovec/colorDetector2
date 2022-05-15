import os
from Extension import method

def colors():
    return 'red green blue yellow fiolet'

def search(color):
    print('Avalible colors for this programm is {}'.format(colors()))
    method(color)
    
search('green')
