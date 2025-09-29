from itertools import permutations
class LetterPermutator:
    def __init__(self, letters):
        if isinstance(letters, LetterPermutator):
            self._letters = letters._letters
        elif isinstance(letters, str):
            self._letters = self._letters_validation(letters)
        else: 
            raise TypeError("Invalid type for letters") 
        
    @property
    def letters(self): return self._letters

    @letters.setter
    def letters(self, alphabets):
        self._letters = self._letters_validation(alphabets)

    def _letters_validation(self, letters):
        if not all(ch.isalpha() for ch in letters):
            raise TypeError("Not all are Letters")
        return letters
    
    def make_possible_strings(self):
        for p in permutations(self._letters):
            print(''.join(p))
        


        
          
