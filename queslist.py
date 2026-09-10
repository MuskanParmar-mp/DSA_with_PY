'''a = [12, 12, 45, 45, 67, 78]

print(a)





a = [12, 12, 45, 45, 67, 78]

b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)


#2


a = [12, 12, 45, 45, 67, 78]

b = []

for i in a:
    b.append(i + 30)

print(b)







#4

a = [12, 12, 45, 45, 67, 78]

b = []

for i in a:
    if i % 2 == 0 and i % 3 == 0:
        b.append(i)

print(b)





#4



a = [12, 12, 45, 45, 67, 78]

b = list(filter(lambda i: i % 2 == 0 and i % 3 == 0, a))

print(b)

a = [12, 12, 45, 45, 67, 78]

b = [i for i in a if i % 2 == 0 and i % 3 == 0]

print(b)






# 5
a = [12, 12, 45, 45, 67, 78]

count = 0

for i in a:
    if i % 2 == 0:
        count += 1

print(count)



#6....

a = [12, 12, 45, 45, 67, 78]

total = 0

for i in a:
    if i % 2 == 0:
        total += i

print(total) '''




# Ques 1

a = [12, 12, 45, 45, 67, 78]

print(a)



# ques 2

b = []
for i in a:
    if i not in  b:
        b.append(i)
print(b)


# ques 3

b = []
for i in a:
    b.append(i + 30)
print(b) 


#list compre.....
b = [i + 30 for i in a]

print(b)




# ques 4 

#normal loop
b = []

for i in a:
    if i % 2 == 0 and i % 3 == 0:
        b.append(i)

print(b)


# filter

b = list(filter(lambda i: i % 2 == 0 and i % 3 == 0, a))

print(b)

# list compre

b = [i for i in a if i % 2 == 0 and i % 3 == 0]
print(b)





# ques 5

count = 0
for i in a:
    if i % 2 == 0:
        count += 1
print(count)



# ques 6

total = 0
for i in a:
    if i % 2 == 0:
        total += i
print(total)


# ques 7

a.insert(1, 340)
a.insert(2, 500)

print(a)


# ques 8

total = 0
count = 0

for i in a:
    if i > 60:
        total += i
        count += 1

print("Sum =", total)
print("Count =", count)


# ques 9 

product = 1

for i in a:
    if i % 2 == 0:
        product *= i

print(product)



a = [12,13,14,15,16]
a[3:3]= 300





list = []