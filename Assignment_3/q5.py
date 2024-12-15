# 5. Write a Python program to get a single string from two given strings, separated  by a space and swap the first two characters of each string.   
# Sample String : 'abc', 'xyz'  
# Expected Result : 'xyc abz'

def swap_chars(str1, str2):
    return str2[:2]+str1[2:]+" "+str1[:2]+str2[2:]

print(swap_chars('abc', 'xyz'))  # Expected Result : 'xyc abz'