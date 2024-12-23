# 10. Write a Python program to find the list of words that are longer than n from a given list of words.

def find_long_words(words,n):
    return [s for s in words if len(s) > n]

words = ["Hello", "World", "Python", "AI", "Machine Learning"]

print(find_long_words(words, 5))  # Output: ['Python', 'Machine Learning']