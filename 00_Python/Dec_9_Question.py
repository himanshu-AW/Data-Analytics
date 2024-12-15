# Q1: Write a python program to calculate dog age in dog's year. Note for the first Two year, a dog year is equal to 10.5 of human years. After that , each dog year equals 4 human years.
# Expected output:-
# input a dog's age is human year = 15
# The dog's age in dog's year is 73

def cal_dog_age(human_age):
    if human_age <= 2:
        return human_age * 10.5
    else:
        return (human_age - 2) * 4 + 21
    
dog_age = cal_dog_age(15)
print("The dog's age in dog's year is", dog_age)

# Q2: Write a python program to convert a list of characters into a string.

characters = ['H', 'e', 'l', 'l', 'o']
string = ''.join(characters)
print("The string is", string)

# Q3: Write a python program to create a lambda function that adds 15 to given no. passed is in as an argumnet, also create a lambda function that multiply argument x with argument y and print the result.

add_fifteen = lambda x : x + 15
multiply = lambda x, y: x * y
print("Result of adding 15 to 10 is:", add_fifteen(10))
print("Result of multiplying 10 and 5 is:", multiply(10, 5))