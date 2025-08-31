class  WordsCount:
   def __init__(self, sentence):
      if isinstance(sentence, str):
         self._sentence = sentence
      elif isinstance(sentence, WordsCount):
         self._sentence = sentence._sentence
      else:
         raise TypeError("sentence type is not valid")
        
   @property
   def sentence(self): return self._sentence

   @sentence.setter
   def sentence(self, wordslist):
      if not isinstance(wordslist, str):
        raise TypeError("for changing the sentence, type is invalid")
      self._sentence = wordslist

   def _words_formation(self):
      return self._sentence.split()     

   def word_repetation_times(self):
      words = self._words_formation()
      count = {}  
      for word in words:
           count[word] = count.get(word, 0) + 1      
      for word, c in count.items():
            print(f"{c} time the \"{word}\" in the sentence")

   def __str__(self):
      return f"your provided list of words was {str(self._sentence)}" 
   
  
   

     


        



          




             
           

   







