# linear  search algo

#li = [-11,-2,19,37,64,-18]

'''print("enter list element")
li = list(map(int,input().split()))

print("enter target element")
target = int(input())
result = -1
size = len(li)
for i in range(size):
    if (li[i]==target):
        result = i
        break
print(result)   '''




# Binary Search

li = [4, 7, 8, 10, 23, 45, 78]

target = 23

start = 0
end = len(li) - 1

while start <= end:

    mid = (start + end) // 2

    if li[mid] == target:
        print(mid)

    elif li[mid] > target:
        end = mid - 1
        break
    else:
        start = mid + 1

else:
    print("Element not found")

