import random

class Jumper:
    def __init__(self):
        self._jumper_try = 4

    '''This will draw the jumper'''
    def draw_jumper_try(self):
        jumper = "replace."
        if  self._jumper_try == 4:
            jumper = "  ___\n /___\\\n \\   /\n  \ /\n   o\n  /|\\\n  / \\\n\n^^^^^^^"
        elif self._jumper_try == 3:
            jumper = "\n /___\\\n \\   /\n  \ /\n   o\n  /|\\\n  / \\\n\n^^^^^^^"
        elif self._jumper_try == 2:
            jumper = "\n \\   /\n  \ /\n   o\n  /|\\\n  / \\\n\n^^^^^^^"
        elif self._jumper_try == 1:
            jumper = "\n  \ /\n   o\n  /|\\\n  / \\\n\n^^^^^^^"
        elif self._jumper_try <= 0:
            jumper = "\n   X\n  /|\\\n  / \\\n\n^^^^^^^"
        return jumper

    '''this is for incorrect letter'''
    def remove_jumper_try(self):
            self._jumper_try -= 1
    
    def return_try(self):
        '''If in thr last try the result is 0 then the ganme ends'''
        return self._jumper_try