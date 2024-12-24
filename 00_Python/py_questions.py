# Write a program which will find all such numbers which are divisible
# by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence
# on a single line.


def find_numbers(start, stop, divisible, not_multiple):
    """
    :param start: start of search range
    :param stop: end of search range
    :param divisible: find numbers which are divisible by this number
    :param not_multiple: exclude numbers that are a multiple of this number
    :return: list of numbers meeting above criteria
    """
    result = []
    for i in range(start, stop + 1):
        if i % divisible == 0 and i % not_multiple != 0:
            result.append(i)
    return result


# print(find_numbers(2000, 3200, 7, 5))
# print(find_numbers(0, 100, 7, 5))




# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input


def calc_factorial(*args):
    """
    :param args: compute the factorial of each supplied number
    :return: a comma-separated sequence of results
    """
    result = []
    for arg in args:
        answer = 1
        for i in range(1, arg + 1):
            answer = answer * i
        result.append(str(answer))
    return result


# print(",".join(calc_factorial(5, 8, 23)))

# With a given integer number n, write a program to generate a dictionary
# that contains (i, i*i) such that is an integer number between 1 and n
# (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Consider use dict()


def generate_squares(n):
    """Generate a dictionary containing range(1, n) entries with number squared as value

    :param n: upper end of range for generating dictionary populated with i: i*i
    :return:
    """
    result = {}
    for i in range(1, n + 1):
        result.update({i: i * i})
    return result

# print(generate_squares(8))




# Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.


def input_to_tuple_and_list():
    nums = input("Input comma-separated integers\n> ").split(",")
    print(nums)
    print(tuple(nums))
    # return nums, tuple(nums)


# input_to_tuple_and_list()




# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints:
# Use __init__ method to construct some parameters

class StringProcessor:
    def __init__(self):
        self.input_string = ""  # Initialize with an empty string

    def getString(self):
        """Method to get a string from console input."""
        self.input_string = input("Enter a string: ")

    def printString(self):
        """Method to print the string in uppercase."""
        print(self.input_string.upper())


# Test function to demonstrate class functionality
def test_string_processor():
    sp = StringProcessor()  # Create an instance of StringProcessor
    sp.getString()          # Get input from user
    print("String in uppercase:")
    sp.printString()        # Print the string in uppercase


# Run the test function
# if __name__ == "__main__":
#     test_string_processor()




# Write a program that calculates and prints the value according
# to the given formula.
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program
# in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is
# given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
# Hints:
# If the output received is in decimal form, it should be rounded off
# to its nearest value (for example, if the output received is 26.0,
# it should be printed as 26) In case of input data being supplied to
# the question, it should be assumed to be a console input.
import math


def calculation():
    c = 50
    h = 30
    nums = input("Please enter comma-separated integers: ").split(",")
    output = []
    for num in nums:
        output.append(str(int(math.sqrt((2 * c * int(num)) / h))))
    print(",".join(output))


# calculation()


# Write a program which takes 2 digits, X,Y as input and generates
# a 2-dimensional array. The element value in the i-th row and j-th
# column of the array should be i*j. Go to the editor
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0],
#  [0, 1, 2, 3, 4],
#  [0, 2, 4, 6, 8]]
# Hints:
# Note: In case of input data being supplied to the question,
# it should be assumed to be a console input in a comma-separated form


def array(rows, columns):
    result = []
    for i in range(rows):
        sub_list = []
        for j in range(columns):
            sub_list.append(i * j)
        result.append(sub_list)
    print(result)


# array(3, 5)

# Write a program that accepts a comma separated sequence of
# words as input and prints the words in a comma-separated
# sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
# Hints:
# In case of input data being supplied to the question, it should
# be assumed to be a console input.


# def sort_words(string):
#     print(",".join(sorted(string.split(","))))


# sort_words("without,hello,bag,world")
def sort_words(string):
    print(",".join(sorted(string)))


# sort_words(["without","hello","bag","world"])



# Write a program that accepts sequence of lines as input and
# prints the lines after making all characters in the sentence
# capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.


def capitalise(string):
    print(string.upper())


# capitalise("hello world\npractice makes perfect\nsense")





def remove_dups_sort(string):
    for word in sorted(set(string.split())):
        print(word, end=" ")


remove_dups_sort("hello world and practice makes perfect and hello world again")



# to get all solution https://github.com/BrettMcGregor/w3resource.git