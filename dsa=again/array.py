# Dsa [ARRAY]

# It is a data structure, with multiple elements

#===============================================================================================
# Array Traversal
#===============================================================================================

# fetch the element 1 by 1

arr = [10,20,30]
for i in range(len(arr)):
    print(arr[i])


# Insertion
arr = [10,20,30]
print(arr.insert(1,50))


#  Deletion




#Find maximum
arr = [20,41,63,96,19,46,81]
max = arr[0]

for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
print(max) 


# find minimum

a = [31,65,85,26,5,26]
min = a[0]

for i in range(len(a)):
    if a[i] < min:
        min = a[i]
print(min)    



# sum of array
 
a = [1,2,3,4]
sum = 0

for i in a:
    sum += i
print(sum)    



# linear search
a = [31,65,85,26,5,26]

target = 5
for i in range(len(a)):
    if a[i] == target:
      print(i)


      