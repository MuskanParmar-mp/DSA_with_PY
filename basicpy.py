print("Hello World");

#Input
a = int(input("Enter your name: "))
print(a)

age = int(input("enter your age:")) 
if (age >= 18):
    print("you vote")
else:
    print("you cannot vote")    




a = [12, 12, 45, 45, 67, 78]

b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)
