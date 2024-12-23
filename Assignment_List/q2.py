# 2. Write a Python program to multiplies all the items in a list. 
num = [1,2,3,4,5]
product=1
for x in num:
    product *= x
print(product)

# or
# from functools import reduce
# sum_of_items = reduce(lambda x,y:x*y,num)
# print("Sum of all items:", sum_of_items)