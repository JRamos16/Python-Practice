#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
#and makes a new list of only the first and last elements of the given list. 
#For practice, write this code inside a function.

def first_and_last(input_list):
    new_list = []
    for element in range(len(input_list)): #we are using the range and len() bc we are accessing indeces now, not just elements 
        if element == 0 or element == len(input_list) - 1: #accessing the first and last elements 
            new_list.append(input_list[element])
    return(new_list)


numbers = [5, 10, 15, 20 ,25]
answer = first_and_last(numbers)
print(answer)
