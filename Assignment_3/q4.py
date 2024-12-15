# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.   
# Sample String : 'restart'  
# Expected Result : 'resta$t'  

def replace_char(str,newChar):
    first = str[0]
    return first + str[1:].replace(first, newChar)

print(replace_char('restart', '$'))
print(replace_char('characteristic', '-'))
print(replace_char('title of titanic', '@'))
