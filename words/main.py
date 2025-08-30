from words_count import WordsCount

if __name__ == "__main__":
       try:
          sen1 = WordsCount("happy birthday , happy birthday to me !! ")
          sen2 = WordsCount(" ")
          print(sen1)
          print(sen2)

       except(TypeError) as e:
          print (f"Error:{e}")
       except(ImportError) as e:
           print(f"Error: module words is not found")   
            