class Index:
    def __init__(self, seqeuence):
        if isinstance(seqeuence, Index): self._seqeuence = seqeuence._seqeuence
        elif isinstance(seqeuence, str): self._seqeuence = seqeuence
        else: raise TypeError("Invalid seqeuence type")

    @property
    def seqeuence(self): return self._seqeuence

    @seqeuence.setter
    def seqeuence(self, seq):
        if not isinstance(seq, str): raise TypeError("Invalid seqeuence for mutation")
        self._seqeuence = seq

    def __len__(self):
        return len(self.seqeuence)

    def __getitem__(self, j):
        if j < 0: j += len(self)
        if 0 <= j < len(self):
            return self._seqeuence[j]
        else: raise IndexError("index out of bound")

    def __str__(self):
        return f"seqeuence is {self._seqeuence}"    
