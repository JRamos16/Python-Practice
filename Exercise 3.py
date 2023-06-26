#Take a list, say for example this one:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements 
#of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []
user_list = []

#prints out a new list w/numbers that are less than 5
for elements in a: 
    if elements < 5:
        x.append(elements)
        x.sort()
print(x)

#prints out a new list with numbers that are less than user input
user_input = int(input("Please enter a number: "))
for numbers in a: 
    if numbers < user_input: 
        user_list.append(numbers)
        user_list.sort()
print(user_list)
