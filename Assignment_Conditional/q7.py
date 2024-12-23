# 7. Write a Python program that prints each item and its corresponding type from the following list.  
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'Python foundation', (0, -1), [5, 12], {"class":'V', "section":'A'}] 

datalist = [1452, 11.23, 1+2j, True, 'Python foundation', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for item in datalist:
    print(f"Item : {item}, Type of {type(item)}")