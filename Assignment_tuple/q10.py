# 10. Write a Python program to check whether an element exists within a tuple.


my_tuple = (10, 20, 30, 40, 50)

# Element to check
element = 30

# Check existence
if element in my_tuple:
    print(f"Element {element} exists in the tuple.")
else:
    print(f"Element {element} does not exist in the tuple.")
