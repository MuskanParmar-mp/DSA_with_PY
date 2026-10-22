# TWO SUM ------------------------------------------------



#Approach 1 — Brute Force
arr = [2,7,11,13]
target = 9

for i in range(len(arr)):
    for j in range(i+1,len(arr)):

        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])


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







# Missing Number ======================================================================

