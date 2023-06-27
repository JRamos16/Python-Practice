#Ask the user for a string and print out whether this string 
#is a palindrome or not. (A palindrome is a string that reads
#the same forwards and backwards.)

#This code works with just words, need to look back at it later to make
#it work with phrases too.

user_word = input("Please enter a word to check: ")
reversed_word = user_word[::-1]

if user_word == reversed_word:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")