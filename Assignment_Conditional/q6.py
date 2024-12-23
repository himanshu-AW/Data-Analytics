# 6. Write a Python program to count the number of even and odd numbers from a series of numbers. 
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)   
# Expected Output :  
# Number of even numbers : 5  
# Number of odd numbers : 4  

def count_even_odd(number):
    even_count = 0
    odd_count = 0
    for num in number:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count, odd_count = count_even_odd(numbers)
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")