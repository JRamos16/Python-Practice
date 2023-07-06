#Write a program (function!) that takes a list and 
#returns a new list that contains all the elements 
#of the first list minus all the duplicates.


def no_duplicates(nums):
    return list(set(nums))


user_list = [1, 2, 3, 4, 5, 3, 2, 3, 1, 1, 10]
print(no_duplicates(user_list))
