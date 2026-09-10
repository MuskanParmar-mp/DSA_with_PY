'''n = int(input("Enter an number:"))
i=2
while i<=n:
    print(i,end=" ")
    i=i+2'''

# sum of n even number

'''n = int(input("Enter how many even number:"))
i=2
sum=0
while i<=n:
    print(i,end=" ")
    sum=sum+i
    i=i+2

    print("sum of even number till",n," is:",sum)'''

# n odd number

'''n = int(input("Enter an number:"))
i=1
while i<=n:
    print(i,end=" ")
    i=i+2'''

# sum of n odd number

'''n = int(input("Enter how many even number:"))
i=1
sum=0
while i<=n:
    print(i,end=" ")
    sum=sum+i
    i=i+2

    print("sum of odd number till",n," is:",sum)'''



#n=10 , o/p=2,4,6,8,10

'''n = int(input("Enter how many even number:"))
i=2
while i<=n:
    if i <= (n-2):
     print(i,end='+')
    else:
       print(i)
    i=i+2 


    #

n = int(input("Enter how many even number:"))
i=2
sum=0
while i<=n:
    sum=sum+i
    if i <= (n-2):
     print(i,end='+')
    else:
       print(i,end='=')
    i=i+2 
print(sum)'''

#count total no of digit in given number

'''n = int(input("Enter how many even number:"))
total-digit=0
while(n>0):
    total-digit=total-digit+1
    tot'''


#palindrome

'''n = input("Enter how many even number:")
if n == n[:: -1]:
    print("palindrome")
else:
    print("not")    '''




#-----------------------------------------------------------------------------------
# for loop
#----------------------------------------------------------------------------------


#print n natural number
'''n = int(input("Enter any number:"))
for  i in range(1, n+1):
    if i<n:
        print(i,end=',')
    else:
        print(i)    '''

#print n natural number sum 
'''n = int(input("Enter any number:"))
for  i in range(1, n+1):
    if i<n:
        print(i,end=',')
    else:
        print(i)  '''  


#list
'''l = (1,2,3,4,5,6,7,8)
l1= []
for i in l:
    l1.append(i)
    print(tuple(l1))'''

#dictionary
'''d = { 'name':'muskan','age':20,'active':True}
for i in d:
    print(i) '''


#check given no is armstrong or not

'''n = int(input("Enter any value:"))
td=0
x=y=n
sum=0
while n>0:
    td=td+1
    n=n//10
while x>0 :
    td=x%10
    sum = sum+td**td
    x=x//10
if y==sum:       
    print("armstrong")
else:
    print( "not armstrong")  '''


'''n = int(input("Enter an number:"))
i=1
while i<=n:
    print(i,end=" ")
    i=i+2 '''




#-----------------------------------------------------------------------------------
# for loop
#----------------------------------------------------------------------------------

'''n=5
for i in range(1,6):
    print(i,end=' ')'''    #1 2 3 4 5
 
n=5
for j in range(1,n+1):
    for i in range(1,n+1):
        print(i,end=' ')
    print()    