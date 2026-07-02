# def rec(s, n):
#     if s == n:
#         return

#     print(s, end=" ")
#     rec(s + 1, n)

# rec(1, 11)





# n = int(input("Enter a no:"))
# fact = 1

# for i in range(1, n+1):
#     fact *= i

# print("Factorial =", fact)


 
# def fact(n):
#     if n==1:
#         return n
#     return n*fact(n-1)

# fact(5);        




# n = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(n * i)




# generate table using recursion

def tbl(n,l):
    if l == 0:
        return 1

    tbl(n,l-1)
    print(n*l)    