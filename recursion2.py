# generate table using recursion

def tbl(n,l):
    if l == 0:
        return 1

    tbl(n,l-1)
    print(n*l)    

tbl(4,10)    