# 8. Write a Python function that takes a list of words and returns the length of the longest one.  

def longest_word_length(words):
    return max(len(word) for word in words)

words = ["Hello", "World", "Python", "AI"]

print(longest_word_length(words))  # Output: 6
