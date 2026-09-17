li = [-11,-2,19,37,64,-18]
k = 3

for i in range(0,len(li) - k +1):
    for j in range(i,i + k):
        print(j,end=" ")