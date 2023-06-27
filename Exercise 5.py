#Take two lists, say for example these two:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains
#only the elements that are common between the lists (without duplicates). 
#Make sure your program works on two lists of different sizes.

#So the way that this is working is that I am using set 
#to iterate through each array and getting rid of any repeating elements
#then, using the &, we can intersect the two lists and get the common 
#elements, pretty fast, pretty cool

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_elements = list(set(list1) & set(list2))
print(common_elements)

