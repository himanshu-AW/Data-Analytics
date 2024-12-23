# 10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged. 

def exchange_first_last_char(str):
    return str[-1]+str[1:len(str)-1]+str[0]

print(exchange_first_last_char("Hello World"))  # Output: "olleH dlroW"