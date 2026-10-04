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





    n=int(input("enter rows:"))
i=1
while i<=n:
    print('*'*n)
    i=i+1


'''n=int(input("enter rows:"))
i=1
while i<=n:
    print('*'*i+''*(n-i))
    i=i+1'''


'''n=int(input("enter rows:"))
i=1
while i<=n:
    print(' '*(n-i)+'* '*i)
    i=i+1'''


'''n=int(input("enter rows:"))
i=1
while i<=n:
    print(' '*i+'*'*(n-i))
    i=i+1'''


'''n=int(input("enter rows:"))
i=n
while i>=1:
    print(' '*(n-i)+'*'*i)
    i=i-1 '''



#-----------------------------------------------------------------------------------
# for loop
#----------------------------------------------------------------------------------


'''n=5
for j in range(1,n+1):
    for i in range(1,j+1):
        print(i,end=' ')
    print() 


n=5
for j in range(1,n+1):
    for i in range(1,j+1):
        print(2*i,end=' ')
    print()   



    
n=5
for j in range(1,n+1):
    for i in range(1,j+1):
        print(2*i-1,end=' ')
    print() '''  


'''n=5
x=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(x,end=' ')
        x=x+1
    print()'''










    
# alfabet pettern 


'''num=int(input("enter number of row:"))
for i in range(1,num+1):
     ch='A'
     for _ in range(1,i+1):
         print(ch,end=' ')
         ch=chr(ord(ch)+1)
     print()  '''



#  one letter eft 
'''num=int(input("enter number of row:"))
for i in range(1,num+1):
     ch='A'
     for _ in range(1,i+1):
         print(ch,end=' ')
         ch=chr(ord(ch)+2)
     print()   
    '''
    
    
'''num=int(input("enter number of row:"))
ch='A'
for i in range(1,num+1):
     for _ in range(1,i+1):
         print(ch,end=' ')
         ch=chr(ord(ch)+1)
     print()'''




