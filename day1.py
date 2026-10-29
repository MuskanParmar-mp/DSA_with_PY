#Second Largest Element


# approach 1 : sorting -----------------------------------

'''arr = [10,4,64,25,75,22,83]
arr.sort()
print(arr[-2])

# approach 2 :Without sorting-----------------------------------

arr =  [10,3,4,23,20]
largest = float('-inf')
second_l = float('-inf')

for num in arr:
    if num > largest:
        second_l = largest
        largest = num 
    elif num > second_l  and num != largest:
        second_l = num
print(second_l)'''



#=============================================================================
# Move all Zeroes to End
#=============================================================================


# Simple Approach

'''arr = [0,1,4,5,0,21,0]
result = []

for num in arr:
    if num != 0 :
        result.append(num)

count_zero = arr.count(0)

for i in range(count_zero):
    result.append(0)

print(result)
'''

# Better Interview Approach — Two Pointer


arr = [0,1,0,3,12]

pos = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos] == arr[i]
        pos += 1

while pos < len(arr):
    arr[pos] = 0
    pos += 1
print(arr)    




#=============================================================================
# Remove Duplicates
#=============================================================================


# using set

a = [1, 2, 2, 3, 4, 4, 5]
res = list(set(a))

print(res)



# without set

a =  [1, 2, 2, 3, 4, 4, 5,6]
result = []

for num in a:
    if num not in result:
        result.append(num)
print(result)        



#=============================================================================
# Remove Duplicates
#=============================================================================



arr = [1, 2, 2, 3, 1, 2, 4]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)            




#Approach 2 — Dictionary

arr = [2, 7, 11, 15]
target = 9
seen = {}

for num in arr:
    needed = target - num

    if needed in seen:
        print(needed,num)
        break
    seen[num] = True



arr = [2,7,11,13,15]
target = 9

for i in range(len(arr)):
    for j in range(i+1,len(arr)):

        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])




# linear search
a = [31,65,85,26,5,26]

target = 5
for i in range(len(a)):
    if a[i] == target:
      print(i)



a = [31,65,76,42,23]

target = 5
for i in range(len(a)):
    if a[i] == target:
      print(i)
