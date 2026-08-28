# From Basic to Advance 

'''name = "Muskan"
print(name)
print(name[0])           # indexing
print(name[4])           # indexing

print(name[-1])           # Negetive indexing
print(name[-2])           # Negetive indexing
print(name[-6])           # Negetive indexing

#--------------------------------------------------------------------------------------------------------------------------------------------

               #String Length

print(len(name))



#--------------------------------------------------------------------------------------------------------------------------------------------

               #Slicing 

# syx: string[start:end] 

print(name[0:3])
print(name[3:6])

print(name[::-1])         # reverse string'''




# for loop se  Stirng traverse

'''s = "Python"

for ch in s:
    print(ch)


for i in range(len(s)):        #with index no
    print(i,s[i])'''

#############################################################################################3
'''course = "Programming"
for ch in course:
    print(ch)


ch = "m"

if ch in 'aeiou':
    print("Vowel")
else:
    print("consonent")    


edu = "education"
vowel = 0
consonant = 0 

for ch in edu:
    if ch in "aeiou":
        vowel += 1
    else:
        consonant += 1    
print("Vowel = ", vowel)
print("consonant = ", consonant)



text = "Programmingcode"

target = input("Enter Char:")
count = 0 

for ch in text:
    if ch == target:
        count += 1
print(count)        



s = "hello"
reverse = ""

for ch in s:
    reverse = ch + reverse
print(reverse)    '''



###########################################################################################


#count()   means frequency check 

s = "banana"
#print(s.count("a"))
#print(s.count("n"))            #simple count


target = "a"
count = 0

for ch in s:
    if ch == target:               #count by loop
        count += 1
print(count)        




#-------------------------------------------------------------------------------------------------------------------------------------

#Dictionary 

'''student = {
    "name": "Muskan",
    "age": 20,
}
print(student)


  #count by dictionary

s = "banana" 
freq={}                                      #count by dictionary

for ch in s:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

print(freq)



fruit = "apple"

frequecy = {}

for ch in fruit:
    if ch in frequecy:
        frequecy[ch] = frequecy[ch] + 1
    else :
        frequecy[ch] = 1

print(frequecy)   '''         
            



#--------------------------------------------------------------------------------------------------------

# Palindrome

'''s = input("Enter String")

rev = s[::-1]

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome") '''


# Two Pointer 

'''s = input("Enter a String: ")
left = 0
right = len(s)-1

while left < right:
    if s[left] != s[right]:
        print("not a palindrome")
        break

    left = left + 1
    right = right - 1
else:
    print("its palindrome") '''


#---------------------------------------------------------------------------------------------------

# Anagram using sorting

'''s1 = input("eneter a string: ")
s2 = input("eneter a string: ")

if sorted(s1) == sorted(s2):
    print("anagram")
else:
    print("not anagram") '''


# Anagram using frequency

'''s1 = "listen"
s2 = "silent"

freq1 = {}
freq2 = {}

for ch in s1:
    if ch in freq1:
        freq1[ch] += 1
    else :
        freq1[ch] = 1


for ch in s2:
    if ch in freq2:
        freq2[ch] += 1
    else :
        freq2[ch] = 1

if freq1 == freq2:
    print("anagram")
else :
    print("not anagram")   '''     

            
       



# example - 2

'''p1 = "apple"
p2 = "papel"

fr1 = {}
fr2 = {}

for ch in p1:
    if ch in fr1:
        fr1[ch] += 1
    else:
        fr1[ch] = 1

for ch in p2:
    if ch in fr2:
        fr2[ch] += 1
    else:
        fr2[ch] = 1             

if fr1 == fr2 :
    print("ha anagram")
else:
    print("n anagram")    '''



#---------------------------------------------------------------------------------------------------------

# Duplicate characters

'''s = "programming"
fre = {}

for ch in s:
    if ch in fre:
        fre[ch] += 1
    else:
        fre[ch] = 1

for ch, count in fre.items():
    if count > 1:
        print(ch)'''





# First Non - Repeating Character

'''st = "aabbcbbe"
freq = {}

for ch in st:
    if ch in freq:
        freq[ch] += 1
    else :
        freq[ch] = 1

for ch in st:
    if freq[ch] == 1:
        print(ch)
        break '''





# Practice ques 

# Q1. fin duplicate characterstics

'''s = "programming"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch, count in freq.items():
    if count > 1:
        print(ch) 



# Q2 : First non repeating character

m = "swiss"
freq = {}

for ch in m:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1


for ch in m :
    if freq[ch] == 1:
        print(ch)
        break'''





#-----------------------------------------------------------------------------------------------------

# Substring topic (DSA)

'''s = "python"
print(s[1:4])



if 'yth' in s:
    print("found")
else:
    print("not found")    



print(s.find(('th')))
print(s.find("xyz"))


# Practice ques

m = "programming"

if "gram" in m:
    print("found")




# Q2
print(m.find("gram"))
    

# Q3
b = "banana"

count = 0 

for ch in b:
    if ch == "a":
        count += 1
print(count)        '''




#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''s = "car"

left = 0 
right = len(s) - 1

while left < right:
    if s[left] !=  s[right]:
        print("not palin")
        break
    

    left = left + 1
    right = right - 1
else:
    print("palindrome")   '''


#-----------------------------------------------------------------------------------------------


# valid palindrome 

'''s = input("enter string : ")

s = s.lower()
clean = ""

for ch in s:
    if ch.isalnum():
        clean = clean + ch

left = 0
right = len(clean) - 1

while left  < right:

    if clean[left] != clean[right]:
        print("Not Palindrome")
        break

    left += 1
    right -= 1

else :
    print("Valid Palindrome")    


#-----------------------------------------------------------------------------------

#remove duplicate char

s = "prograamming"

res = ""

for ch in s:
    if ch not in res:
        res += ch

print(res) 


#--------------------------------------------------------------------

#reverse a word

s = input("Eneter a strig : ")

words = s.split()

words.reverse()

result = " ".join(words)

print(result)'''


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#longest word

s = "muskan"
words = s.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("losgest word : " , longest)
   








          
