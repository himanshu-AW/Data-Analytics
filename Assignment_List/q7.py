# 7. Write a Python program to remove duplicates from a list.   

def remove_duplicates(lst):
    return list(set(lst))

lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
print(remove_duplicates(lst))