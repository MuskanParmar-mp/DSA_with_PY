
'''a = [10, 20, 30, 40]

total = 0


for i in range(len(a)):
     total += a[i]

print(total) 

#----------------------------------------------------------

li = [12,45,67,89]
total = 0

for i in range(len(li)):
     if li[i] > 50:
          total += li[i]
print(total)          



li = [12,45,67,89]
total = 0

for i in range(len(li)):
     if li[i] < 50:
          total += li[i]
print(total)

#===============================================================================================

li = [12,45,67,89]
total = 0

for i in range(len(li)):
     if li[i] % 2 == 0:
          total += li[i]
print(total)


#===================================================================================================

li = [12,45,67,89]
count = 0 

for i in range(len(li)):
     count += 1
print(count)



li = [12,45,67,89]
sum = 0 

for i in range(len(li)):
     if li[i] % 5 == 0:
          sum += li[i]
print(sum)'''


#=================================================================================================

a = [12,34,56,34,45]
l = []

for i in a :
     if i % 2 != 0:
          l.append(i)
print(l)     





# using filter


a = [12,34,56,34,45]
b = list(filter(lambda i : i % 2 == 0,a))
print(b)



a = [12,34,56,34,45]
b = list(filter(lambda i : i % 2 != 0,a))
print(b)


a = [12,34,56,34,45]
b = list(filter(lambda i : i > 20 ,a))
print(b)

a = [2,4,6]
b = list(map(lambda i: i * 2, a))
print(b)



#=================================================================================

#using list comprehence


a = [12,34,56,34,45]
a = [i+10 for i in a]
print(a)


a = [i for i in a if i % 2 == 0]
print(a)





a = [1, 2,3,4]
b = []

for i in a:
    if i % 2 == 0:
         b.append(i + 20)
    

print(b)



n = int(input())
i = 2
prime = True

while(i <=n//2):
    if(n%i == 0):
        prime = False
        break   
    i = i+1  
    
if (prime == True):
    print("True")
else:
    print("False")   






li = [12,45,67,89]
count = 0 

for i in range(len(li)):
     count += 1
print(count)
