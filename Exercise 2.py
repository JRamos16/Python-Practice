#Ask the user for a number. Depending on whether the
#number is even or odd, print out an appropriate message to the user.
#Includes a few extra things...

number = int(input("Please enter a number: "))
check = int(input("Enter another number: "))

if number % 2 == 0:
    print("This 1st number is an even number")
else: 
    print("This 1st number is an odd number")

if number % check == 0:
    print("These two numbers are divisible by each other")
else: 
    print("These two numbers don't divide evenly")
    
