from birthday_paradox import BirthdayParadox

def run():
    try:
        for n in range(5, 15, 5):
            a = BirthdayParadox()
            #print(repr(a))

            b = BirthdayParadox(a)
            #print(b)

            bp1 = BirthdayParadox(10000, n)
            print(bp1)

        print(b.n)
        print(repr(b))
        b.n = 42
        print(repr(b))
        print(b.repeat)
        print(b.n)

        

    except(ValueError) as e:
        print (f"(Error:{e})")  
    except(ImportError) as e:
        print (f"module not found")

if __name__ == "__main__":

    run()        



