# Q1: Write a python program to calculate dog age in dog's year. Note for the first Two year, a dog year is equal to 10.5 of human years. After that , each dog year equals 4 human years.
# Expected output:-
# input a dog's age is human year = 15
# The dog's age in dog's year is 73

def cal_age(age):
    if age <= 2:
        return age * 10.5
    else:
        return (age - 2) * 4 + 21
    
age = cal_age(15)
print("The dog's age in dog's year is", age)

# Q2: Write a python program to convert a list of characters into a string.

characters = ['H', 'e', 'l', 'l', 'o']
string = ''.join(characters)
print("The string is", string)

# Q3: Write a python program to create a lambda function that adds 15 to given no. passed is in as an argumnet, also create a lambda function that multiply argument x with argument y and print the result.

add_fifteen = lambda x : x + 15
multiply = lambda x, y: x * y
print("Result of adding 15 to 10 is:", add_fifteen(10))
print("Result of multiplying 10 and 5 is:", multiply(10, 5))

# Q4: Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

# user_input = input("Please enter an integer for calculation: ")
user_input = 5
print(int(user_input) + int(user_input*2) + int(user_input*3))



#Q5:  Write a Python program to print the documents (syntax, description etc.)
#  of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.
help(abs)


#Q6:  Write a Python program to print the following string in a specific format (see the output):

# Twinkle, twinkle, little star,
#         How I wonder what you are!
#                 Up above the world so high,
#                 Like a diamond in the sky.
# Twinkle, twinkle, little star,
#         How I wonder what you are

print("Twinkle, twinkle, little star,\n\t\tHow I wonder what you are!\n"
      "\t\t\t\tUp above the world so high\n\t\t\t\tLike a diamond in the sky.\n"
      "Twinkle, twinkle, little star,\n\t\tHow I wonder what you are")

#Q7: Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

import datetime

print(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S %"))