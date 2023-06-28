#Write a program that returns a list that contains only the elements that are 
#common between the lists (without duplicates). Make sure your program works 
#on two lists of different sizes. Write this in one line of Python using at 
#least one list comprehension. 

#I know that there is a faster way doing this using sets but I wanted to see 
#how to use list compressions and generating two random lists 


import random

a = random.sample(range(100), 9) #this spits out a list with 9 elements from 0 to 100
b = random.sample(range(100), 8) #this spits out a list with 8 elements from 0 to 100
print(a)
print(b)

new_list = []
for num in a:
    if num in b and num not in new_list:
        new_list.append(num)
print(new_list)


