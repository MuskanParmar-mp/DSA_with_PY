


arr = [3, 13, 5,  8, 2, 1]
n = len(arr)

for i in range(n):
    for j in range(0, n-i -1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)



a = [ 3,4,12,42,1,3]

size = len(a)

for i in range(size):
    for j in range(0, size - i -1):
        if a[j] > a[j+1]:
            a[j] , a[j+1] = a[j+1], a[j]


print(a)            