#Second Largest Element


# approach 1 : sorting 

arr = [10,4,64,25,75,22,83]
arr.sort()
print(arr[-2])

# approach 2 :Without sorting

arr =  [10,3,4,23,20]
largest = float('-inf')
second_l = float('-inf')

for num in arr:
    if num > largest:
        second_l = largest
        largest = num 
    elif num > second_l  and num != largest:
        second_l = num
print(second_l)





 



    