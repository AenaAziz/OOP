import copy
def main():
    a = [3,2,5]
    b = a
    b.remove(2)
    print(a, b)#alias

    c = [[1,1],[2,3,4]]
    d = copy.copy(c)
    c[1][2] = 5
    d.append(3)
    print(c, d)

    e = [[4, 8], [4,5]]
    f = copy.deepcopy(e)
    f.remove([4,8])
    e[1][0] = 6
    print(e, f)




if __name__ == "__main__":
    main()    
   