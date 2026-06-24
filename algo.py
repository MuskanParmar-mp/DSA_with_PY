# A= [10,3,4,8,9]
# for i in A:
#     print(i)




# A= [11,3,4,8,9]
# for i in range(len(A)):
#     print(i)

# for i in range(len(A)):
#     print(A[i])  



# A = [1,2,3,5,4]
# n = len(A)
# c = 0
# for i in range(n):
#     for j in range(n-1):
#         c = c + 1
#         if A[j]>A[j+1]:
#             t = A[j]
#             A[j] = A[j+1]
#             A[j+1] = t
# print("+++++Output++++++")
# for i in A:
#     print(i,end=" ")
# print("total hits =", c)  




#selection sort  

arr = [9,8,7,6,5]
c=0
def selection(nums):
    n = len(nums)
    global c
    for i in range(n-1):
        chhotu = i

        for j in range(i+1, n):
            c=+1
            if nums[chhotu] > nums[j]:
                chhotu = j

        if chhotu != i:
            t = nums[chhotu]
            nums[chhotu] = nums[i]
            nums[i] = t

    return nums

print(selection(arr))
print("total hits=",c)


