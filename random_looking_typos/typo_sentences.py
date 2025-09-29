import random
class SentenceTypo:
    def __init__(self, sen, times, n):
        if isinstance(sen, SentenceTypo):
            self._sentence = sen._sentence
            self._times = sen._times
            self._n = sen._n
        elif isinstance(sen, str) and isinstance(times, int) and isinstance(n, int):
            self._times_n_validation(times, n)
            self._sentence = sen
            self._times = times
            self._n = n
        else: 
            raise TypeError("invalid types")
        self._typo_lines = random.sample(range(1, self._times+1), self._n)
        self._lines = []
    
    @property
    def sentence(self): return self._sentence

    @property
    def times(self): return self._times

    @property
    def n(self): return self._n

    @sentence.setter
    def sentence(self, letters):
        if not isinstance(letters, str):raise TypeError("invalid type for sentence updation")
        self._sentence = letters
        self._lines = []  

    @times.setter
    def times(self, value):
        if not isinstance(value, int):raise TypeError("invalid type for times updation")
        self._times_n_validation(value, self._n)
        self._times = value
        self._typo_lines = random.sample(range(1, self._times+1), self._n) 
        self._lines = []  

    @n.setter
    def n(self, value):
        if not isinstance(value, int):raise TypeError("invalid type for n updation")
        self._times_n_validation(self._times, value)
        self._n = value   
        self._typo_lines = random.sample(range(1, self._times+1), self._n)
        self._lines = []  

    def _make_some_typo(self): 
        self._lines = []
        for i in range(1, self._times+1): 
            output = self._sentence   
            if i in self._typo_lines:
                idx = random.randint(0, len(self._sentence)-1)
                orig = self._sentence[idx]
                letters = [c for c in "abcdefghijklmnopqrstuvwxyz" if c != orig]
                typo_ch = random.choice(letters)
                output = self._sentence[:idx] + typo_ch + self._sentence[idx+1:]
            self._lines.append((i, output))

    def display(self):
       self._typo_lines = random.sample(range(1, self._times+1), self._n)
       self._make_some_typo()
       for i, line in self._lines:
           print(f"{i}: {line}")

    def _times_n_validation(self, times, n):
        if times < 0 or n < 0: raise ValueError("times and n can not be negative")
        if times < n:raise ValueError("times can not be lesser than n")

    def __str__(self):
        return f"the sentence {self.sentence} is repeated {self._times} with typos in {self._n} lines"        





