# 4. Write a Python program to unpack a tuple in several variables.   

tup = (1, 2, 3, 4, 5)
a, b, *c = tup

print("a:", a)

print("b:", b)

print("c:", c)