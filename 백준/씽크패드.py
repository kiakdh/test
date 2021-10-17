def score(t):
    tlist = list(t)
    k = 0
    s = 0 
    for i in range(len(tlist)):
        if tlist[i] == "O":
            k += 1
            s += k
            print(k)
        else:
            k == 0
            print(k)
    return(s)

    





a = score(input())
print(a)




