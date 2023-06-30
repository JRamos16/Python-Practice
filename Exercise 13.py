#Write a program that asks the user how many Fibonacci numbers to generate 
#and then generates them. Take this opportunity to think about how you can 
#use functions. Make sure to ask the user to enter the number of numbers in
#the sequence to generate.


def fiboacci_generator(user_input):
    fib_seq = [0, 1]
    a = 0
    b = 1
    if user_input == 1: 
        return[0]
    elif user_input > 1:
        for i in range(user_input - 2): #we are doing this since we have the first 2 numbers in the list
            next_num = a + b 
            a = b 
            b = next_num
            fib_seq.append(next_num)
        return(fib_seq)

user_input = int(input("Please enter a number: "))
result = fiboacci_generator(user_input)
print(result)










