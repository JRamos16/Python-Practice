#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
#Write one line of Python that takes this list a and makes a new list that has only the even 
#elements of this list in it.

#I implemented this code two different ways. The first way will only work with this given 
#list but the second way would work with any list. 

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(a[1:len(a):2])

even_list = [number for number in a if number % 2 == 0]
print(even_list)
