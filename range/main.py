from range import Range
try:
 if __name__ == "__main__":
    range1 = Range(2, 5, 1)
    print(list(range1))

    range2 = Range(range1)
    print(list(range2))

    range2.start = -2
    range2.stop = "-4"
    range2.step = "+1"

    print(list(range2))

    range3 = Range()
    print(list(range3))

    range4 = Range("5", -1)
    print(range4)
    print(list(range4))


    range6= Range(5, "2", "-3")
    print(len(range6))
    print(bool(range6))
    print(str(range6))
    print(list((range6)))
   # print(range6[8])

   # range7= Range(5, "k2", "*4")
    #print(len(range7))

    range8 = Range(0, "0", "-8" )
    print(list(range8))

    #range9 = Range(0, -5, 0)
    #print(range9)

    range10 = Range(-9, None, -2)
    print(str(range10))
    print(list(range10))
    print(range10.stop)

    range11 = Range(9)
    print(list(range11))

    rg2 = Range(50, 90, 10)
    for value in rg2:
     print(value)

    rg1 = Range(8, -10, -2)
    for value in rg1:
     print(value)

    #range12 = Range(None, None, None)

except(TypeError, ValueError, AttributeError) as e:
    print(f"Error: {e}")

except(ImportError) as e:
   print(f"could not import range module")    

except Exception as e:

   print(f"Unexpected Error:{e}")    
