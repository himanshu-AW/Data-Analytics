# 9. Write a Python program to find the repeated items of a tuple. 

my_tuple = (1, 2, 3, 4, 5, 2, 6, 3, 7, 3)

repeated_items = set([item for item in my_tuple if my_tuple.count(item) > 1])

print("Repeated items:", repeated_items)
