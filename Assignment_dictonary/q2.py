# Write a Python script to add a key to a dictionary. Go to the editor
#
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

start_dict = {0: 10, 1: 20}


def update_dict(key, value):
    start_dict.update({key: value})
    if input("Enter another record? (Y/n) > ").upper() == "Y":
        update_dict(input("Enter key: "), input("Enter value: "))
    else:
        print(start_dict)


# update_dict(input("Enter key: "), input("Enter value: "))



# Write a Python script to concatenate following dictionaries
# to create a new one.
#
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
dict4 = {}

for d in (dict1, dict2, dict3):
    dict4.update(d)

print(dict4)



# Write a Python script to check if a given key
# already exists in a dictionary

dict1 = {1: 10, 2: 20, "Brett": 30, 4: 40, 5: 50, 6: 60}

if "Brett" in dict1:
    print(True)
else:
    print(False)


# Write a Python program to iterate over dictionaries using for loops.

import random


def create_multiple_lists(name, number, master_dict):
    for i in range(number):
        master_dict.update({name+str(i): random.randint(0, 1000)})
    return master_dict


def iterate_dict():
    master_dict = {}
    create_multiple_lists("item", 5, master_dict)
    for keys, values in master_dict.items():
        print(keys, values)


iterate_dict()


# Write a Python script to generate and print a dictionary
# that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


def generate_dict(n):
    my_dict = {}
    for i in range(1, n + 1):
        my_dict.update({i: i*i})
    print(my_dict)


generate_dict(5)


# Write a Python script to print a dictionary where the keys are
# numbers between 1 and 15 (both included) and the values are
# square of keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


def dict_squares(low, high, power):
    my_dict = {}
    for i in range(low, high + 1):
        my_dict.update({i: i ** power})
    print(my_dict)


dict_squares(1, 15, 2)


# Write a Python script to merge two Python dictionaries.

dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
dict2 = {8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
dict3 = {}

for i in (dict1, dict2):
    dict3.update(i)
print(dict3)

# . Write a Python program to iterate over dictionaries using for loops

dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

for k, v in dict1.items():
    print("{:>3}{:.>7}".format(k, v))



# Write a Python program to sum all the items in a dictionary

dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

values = dict1.values()
print(sum(values))
print(sum(dict1.values()))



# Write a Python program to multiply all the items in a dictionary.


dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

values = dict1.values()
product = 1

for value in values:
    product *= value

print(product)



# Write a Python program to remove a key from a dictionary.

dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

del dict1[3]
dict1.pop(1)
print(dict1)



# Write a Python program to map two lists into a dictionary.

keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']

new_dict = {}

for i in range(len(keys)):
    new_dict.update({keys[i]: values[i]})

print(new_dict)



# Write a Python program to sort a dictionary by key.

adict = {'red': 'x#FF0000', 'green': 'y#008000', 'blue': 'z#0000FF'}

print(sorted(adict.items(), key=lambda x: x[0]))




# Write a Python program to get the maximum and
# minimum value in a dictionary.

dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print(min(dict1.values()))
print(max(dict1.values()))