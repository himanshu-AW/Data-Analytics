# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.   
# Sample String : 'The lyrics is not that poor!'  
# 'The lyrics is poor!'  
# Expected Result : 'The lyrics is good!'  
# 'The lyrics is poor!'  


def replace_not_poor(string):
    # Find the first occurrence of 'not' and 'poor'
    not_i= string.find('not')
    poor_i = string.find('poor')

    # If 'not' precedes 'poor', replace the substring with 'good'
    if not_i != -1 and poor_i != -1 and not_i < poor_i:
        string = string[:not_i] + 'good' + string[poor_i + 4:]

    return string

# Sample Strings
sample1 = 'The lyrics is not that poor!'
sample2 = 'The lyrics is poor!'

# Testing the function
print(replace_not_poor(sample1))  # Expected: 'The lyrics is good!'
print(replace_not_poor(sample2))  # Expected: 'The lyrics is poor!'
