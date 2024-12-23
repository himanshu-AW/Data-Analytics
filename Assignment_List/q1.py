# 1. Write a Python program to sum all the items in a list.   

num = [1,2,3,4,5]
sum=0
for x in num:
    sum += x
print(sum)

# or
# from functools import reduce
# sum_of_items = reduce(lambda x,y:x+y,num)
# print("Sum of all items:", sum_of_items)