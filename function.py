'''def show():
    print("welcome")
 
show() '''

# print n natural    ##################################

'''def naturalno(n):
    for i in range(1,n+1):
        print(i)

x=int(input("Enter natural no:"))
naturalno(x) '''


#######################################################

'''def naturalno(n):
    for i in range(1,n+1):
        print(i)

x=int(input("Enter natural no:"))
res=naturalno(x) 
print(res)'''

#########################################################

'''def naturalno(n):
    for i in range(1,n+1):
        print(i)
        return "hello"

x=int(input("Enter natural no:"))
res=naturalno(x) 
print(res)'''


'''def display():
    return "Hello"

print(display())'''



#WAP to print n even number

'''def even_no(n):
    print("Even numbers are:")
    for i in range(2, n + 1, 2):  
        print(i)

num = int(input("Enter n numbers: "))
even_no(num)   '''   




#WAP to print n odd number
'''def odd_no(n):
    print("Odd numbers are:")
    for i in range(1, n + 1, 2):  
        print(i)

num = int(input("Enter n numbers: "))
odd_no(num)'''



#10 even number
'''def even_no(n):
    print("Even numbers are:")
    for i in range(2, n + 1):  
        print(2*i)

num = int(input("Enter n numbers: "))
even_no(num)   '''   




# WAP to print 10 odd number
'''def odd_no(n):
    print("Odd numbers are:")
    for i in range(1, n + 1):  
        print(2 * i - 1)

num = int(input("Enter n numbers: "))
odd_no(num)''' 


#WAP to print factorial
'''def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact= fact * i 
        print("factorial of", n , "is:", fact)

num= int(input("Enetr a number"))
factorial(num)'''


#######################################################
'''def add(x,y,z):
   print(x)

add(10,20,30)'''


'''def add(*args):
    print(args)
    print(type(args))

add(10,20,30)'''






'''def add(*n):
    sum=0
    for i in n:
        sum=sum+i
    print("sum =", sum)

add(10,20,30)  '''


'''x=(10)
y=10
print(type(x))
print(type(y))

p = 10
print(type(p))
q=(10)
print(type(q))'''


'''def add(*n):
    sum=0
    for i in n:
            sum = sum+i
    print("sum:",sum)

x= eval(input("Enetr any value:"))
add(*x)   '''         




########### 4.

'''def fun(x,y,z):
    print(x)
    print(y)
    print(z)

fun(x=10,z=30,x=60)  '''  



### 5.

'''def fun(x=0,y=0,z=0):
    print(x)
    print(y)
    print(z)

fun(y=20,z=30,x=50)  '''



# 6

'''def display(**n):
    print(n)
    print(type(n))

x=eval(input("Enter keywword value:"))
display(**x)'''




'''def display(**n):
    for i,j in n.items():
        print(i,"=",j)

x=eval(input("Enter keywword value:"))
display(**x)'''





#1. positional argument

'''def add(x,y,z):
    print(x+y+z)

add(10,20,30)    #60  '''


#3. variable length posi argument

'''def add_all(*nums):
    total=0
    for n in nums:
        total = total + n
    print("Sum is:" , total)

add_all(1,2,3,4,5 )    '''




#on the basis of argument and return type
#1.

'''def add(a, b):          
    return a + b        

ans = add(10, 20)
print("Sum is:", ans)'''


#2.

'''def fun(name):          
    print("Hello", name)  
fun("Muskan")'''


#3.



#Scope 

'''x=10
def show():
    x=20
    print(x)
 
    
show()  


#
x=10
def show():
    print(x)

show()
print(x)  


#
x=10
def show():
    x=20
    print(x)

show()
print(x)


#
x=10
def show():
    global x
    x=20
    print(x)

print(x)
show()
print(x)    '''

#
'''x=10
def show():
    x=20
    print(x)

show()'''


'''x=10
def show():
    print(x)
    x=20

show()    #error'''


#
'''x=20
def show():
    x=10
    print(globals()['x'])

show()'''
 
