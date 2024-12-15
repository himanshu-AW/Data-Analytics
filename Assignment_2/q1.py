# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).   
def find_num(min_num, max_num):
    for x in range(min_num, max_num):
        if x % 7 ==0 and x%5==0:
            print(x)
        
find_num(1500,2700)