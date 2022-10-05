from game.terminal_service import Terminalservice
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:
   
    def __init__(self):
        '''to execute program'''
        self._proceed = True
        self._keep_try = True
        self._puzzle = Puzzle()
        self._jumper = Jumper()
        self._terminal_service = Terminalservice()
        
    def start_game(self):
        
        while self._keep_try and self._proceed:
            '''to check the ltter in the try or turn'''
            letter = self._get_inputs()
            self._do_updates(letter)
            self._do_outputs()

    def _get_inputs(self):
        self._puzzle.draw_word_guess()
        jumper_draw = self._jumper.draw_jumper_try()
        self._terminal_service.print_jumper(jumper_draw)

        '''input asking to guess letter'''
        new_letter = self._terminal_service.read_letter("\nGuess a letter [a-z]: ")
        return new_letter
    
    def _do_updates(self, letter):
        proccess_guess = self._puzzle.process_guess(letter)
        if proccess_guess:
            self._jumper.remove_jumper_try()    
        else:
            self._puzzle.draw_puzzle(letter)

    def _do_outputs(self):
        
        self._proceed = self._puzzle.continue_guess_letter()
        
        life = self._jumper.return_try() > 0
        if not life:
            self._keep_try = False
            jumper_draw = self._jumper.draw_jumper_try()
            self._terminal_service.print_jumper(jumper_draw)
            print(f'Game over! Jumper out.')