# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.   
# Sample String : 'The lyrics is not that poor!'  
# 'The lyrics is poor!'  
# Expected Result : 'The lyrics is good!'  
# 'The lyrics is poor!'  


def replace_substring(s):
    s = s.replace('not',"")
    s = s.replace('poor', 'good')
    return s

print(replace_substring('The lyrics is not that poor!'))