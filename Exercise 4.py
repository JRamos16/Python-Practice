#Create a program that asks the user for a number and then prints out 
#a list of all the divisors of that number. (If you don’t know what a 
#divisor is, it is a number that divides evenly into another number. 
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

user_number = int(input("Please enter a number: "))
user_list = []

user_input = range(1, user_number + 1)
print(user_list)

for element in user_input: 
    if user_number % element == 0:
        user_list.append(element)
        user_list.sort()
print(user_list)
