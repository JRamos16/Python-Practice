import random 

random_num = random.randint(2,6)
user_num = 0
print(random_num)
#option = input("Would you like to play a guessing game? Yes/No: ")

while user_num != random_num and user_num != "exit":
    user_num = (input("Please enter a number 0 and 10 or 'exit' to quit: "))
    if user_num == "exit":
        break
    user_num = int(user_num)
    if user_num > random_num:
        print("Your guess is too big, try again!")
    elif user_num < random_num: 
        print("Your guess is too small, try again!")
    else:
        print("You guessed the number!")

