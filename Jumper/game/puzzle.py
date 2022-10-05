import random

class Puzzle:
        def __init__(self):
            self._word_list = ['Climb', 'Search', 'Endure', 'Light', 'Alien', 'Train', 'Random', 
            'Submarine', 'House', 'Siren', 'Police', 'Tiger', 'Shrek', 'Pixar', 'Disney', 'Fish', 
            'Nemo', 'Matrix', 'Fire', 'Snow',]
            self._word_selected = random.choice(self._word_list).lower()
            self._guess_word = [" _ "] * len(self._word_selected)

        def get_word_selected(self):
            return self._word_selected

        def draw_word_guess(self):
            print(f'\n{"".join(self._guess_word)}')
            
        '''If the word is in the word list then it will run otherwise it will be considered as a try'''
        def draw_puzzle(self, letter):
            letters_listed_from_words = list(self._word_selected)
            if letter in letters_listed_from_words:
                self._guess_word[letters_listed_from_words.index(letter)] = letter

        def process_guess(self, letter):
            if letter in self._word_selected:
                return False
            else:
                return True

        
        def continue_guess_letter(self):
            if " _ " in self._guess_word:
                return True
            else:
                print()
                print(f'Game complete!, you guessed the word: "--> {self._word_selected.lower()} <--"')
                return False