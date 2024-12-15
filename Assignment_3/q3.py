# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.   
# Sample String : 'w3resource'  
# Expected Result : 'w3ce'  
# Sample String : 'w3'  
# Expected Result : 'w3w3'  
# Sample String : 'w'  
# Expected Result : Empty String

def get_str(str):
    if len(str)<2:
        return ""
    else:
        return str[:2]+str[-2:]
    
print(get_str('w3resource'))  # Expected Result : 'w3ce'
print(get_str('w3'))  # Expected Result : 'w3w3'
print(get_str('w'))  # Expected Result : Empty String