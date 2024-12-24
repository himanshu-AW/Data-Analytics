# 1. Write a Python script to sort (ascending and descending) a dictionary by value.  

d = { 3: 'c',1: 'a',5: 'e', 2: 'b',  4: 'd' }

# Ascending order

sorted_d = dict(sorted(d.items(), key = lambda val: val[1]))
print("Ascending order by value:", sorted_d)

# Descending order

sorted_d = dict(sorted(d.items(), key = lambda val: val[1]))
print("Descending order by value:", sorted_d)