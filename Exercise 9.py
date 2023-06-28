#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to 
#guess the number, then tell them whether they guessed too low, too high, or exactly right.

#I also included two extra details that intel: 
#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random 

random_num = random.randint(1,9)
user_num = 0
print(random_num)
#option = input("Would you like to play a guessing game? Yes/No: ")
counter = 0
while user_num != random_num and user_num != "exit":
    user_num = input("Please enter a number 0 and 10 or 'exit' to quit: ")
    counter +=1
    if user_num == "exit":
        break
    user_num = int(user_num)
    if user_num > random_num:
        print("Your guess is too big, try again!")
    elif user_num < random_num: 
        print("Your guess is too small, try again!")
    else:
        print("You guessed the number!")
        print("And it took you " + str(counter) + " tries!")

