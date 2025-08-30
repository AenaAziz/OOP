from birthday_paradox import BirthdayParadox

def run():
    try:
        for n in range(5, 105, 5):
            a = BirthdayParadox()
            #print(repr(a))

            b = BirthdayParadox(a)
            #print(b)

            #print(b.n)
            #print(repr(b))
            b.n = 42
        #print(b.repeat)
        #print(b.n)

        c = BirthdayParadox(6, 9)
        print(repr(c))

    except(ValueError) as e:
        print (f"(Error:{e})")  
    except(ImportError) as e:
        print (f"module not found")

if __name__ == "__main__":

     run()        



