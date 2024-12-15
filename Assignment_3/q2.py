# 2. Write a Python program to count the number of characters (character   frequency) in a string.   
# Sample String : google.com'  
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}  

def char_freq(str):
    freq = {}
    for char in str:
        freq[char] = freq.get(char,0)+1
    return freq

str = "google.com"
print(char_freq(str))