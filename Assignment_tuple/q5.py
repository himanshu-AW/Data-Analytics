# 5. Write a Python program to add an item in a tuple.  

t = (1, 2, 3)
l = list(t)
l.append(4)
t = tuple(l)
print(t)