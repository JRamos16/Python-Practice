#Write a program (using functions!) that asks the user for a long string containing multiple words.
#Print back to the user the same string, except with the words in backwards order.

def reversed_order(user_input):
    mod_input = user_input.split()
    reversed = mod_input[::-1] #we are using this to splice a list and get a new list in the reverse order
    #just found out that there is reverse() command in python to do this also lol 
    final_phrase = " ".join(reversed)
    return final_phrase 


user_phrase = input("Tell me a phrase: ")
print(reversed_order(user_phrase))


