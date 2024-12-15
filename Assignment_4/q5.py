# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.   
# Sample List : ['abc', 'xyz', 'aba', '1221']  
# Expected Result : 2 

def count_strings(strings):
    count = 0
    for str in strings:
        if len(str) >= 2 and str[0] == str[-1]:
            count += 1
    return count
print(count_strings(['abc', 'xyz', 'aba', '1221']))  # Expected Result : 2