n = 5
for i in range(1,n+1):                    #1,2,3,4,5
    for x in range(range(i)):             # i=1 - 0 i=2-0, 1
        print("*", end="")

    print()   


for i in range(1, n+1):
    for x in range(1,i+1):
        print(x,end=" ")
    print()     






n = int(input())

if n < 2:
    print(False)
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    print(prime)





    