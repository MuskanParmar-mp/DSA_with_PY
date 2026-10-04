# insertion sort

l = [4, 7, 8, 10, 23, 45, 78]
li = 0
size = len(l)
for i in range(size):
    for j in range(i+1, size):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]



li 



            