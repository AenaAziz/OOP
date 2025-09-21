class MinMax:
    "composition"
    def __init__(self, seq):
        if isinstance(seq, MinMax):
            self._list = seq._list.copy()    
        elif isinstance(seq, (str, list, tuple)):
            self._list = list(seq).copy() 
            self._validation()
        else:
            raise TypeError("Provide sequence") 
        
        if not self._list:
            raise ValueError("Sequence cannot be empty")
        
        self._min, self._max = 0, 0
        self.mini_max_identification()
        
    @property
    def seq(self): return self._list

    @property
    def min(self): return self._min

    @property
    def max(self): return self._max

    @seq.setter
    def seq(self, array):
        if not isinstance(array, (list, tuple, str)): raise TypeError("seq updation is invalid")  
        self._list = list(array).copy()
        self._validation()
        self.mini_max_identification() 
        
    def _validation(self):
        for i, item in enumerate(self._list):
            if isinstance(item, int):
                continue
            elif isinstance(item, str):
                if not item.isdigit(): raise ValueError("seqeuence must contain only integers")
                self._list[i] = int(item)
            else:
                raise TypeError("Seqeuence must contain the set of only integers")
    
    def mini_max_identification(self):
        self._min = self._list[0]
        self._max = self._list[0]

        for i in self._list[1:]:
            if i < self._min:
                self._min = i
            if i > self._max:
                self._max = i

    def __str__(self):
        return f"({self._min}, {self._max})"            





