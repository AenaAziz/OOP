import random

class RandomElement:
    #composition
    def __init__(self, seq):
        if isinstance(seq, RandomElement): self._list = list(seq._list)
        elif isinstance(seq, (list, tuple, str)): 
           self._list = list(seq) 
           self._list_values_validation()
        else: raise TypeError("invalid seqeuence type")

    def _list_values_validation(self):
        for i, item in enumerate(self._list):
         if not isinstance(item, (int, str)): raise ValueError("seqeuece must contain digits")
         if isinstance(item ,str):
            if not item.isdigit(): raise ValueError("seqeuece must contain digits")
            self._list[i] = int(item)  

    def choice(self):
       "pythonic"
       return self._list[random.randrange(len(self._list))]

    def tra_choice(self):
       """traditional"""
       index = random.randrange(len(self._list))
       element = self._list[index]
       return element

