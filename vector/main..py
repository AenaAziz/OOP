from vector import Vectors

if __name__ == "__main__":

    try:

        v = Vectors("6")
       # v["d"] = 8
        #v[2] = "d"
        #v[6] = 34
        v[4] = "12"
        #v[4] = 2

        print(v.dimension)
        print(v.coords)

        w = Vectors(v)

        print(w <= v)  # i didn't use __le__ in vector.py

        print(v + w)

        z = [1,2,3,4,5,6]

        total = sum(v)    #don#t need loop
        print(total)

        print(w + z) 

        t = Vectors("2")

        k = Vectors(5)
        print(v + k)

        u = Vectors(6)
        print(v > u)




    except (TypeError, ValueError, IndexError) as e:
        print(f"Vector error: {e}")   
    except ImportError:
        print("Error: Could not import vector module")
    except Exception as e:
        print(f"Unexpected error: {e}")  
    


     



     