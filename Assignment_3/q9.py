# 9. Write a Python program to remove the nth index character from a nonempty string. 

def rem_nth_idx(str,newStr,n):
    if n < 0 or n > len(str):
        return "Invalid index"
    else:
        return str[:n]+newStr+str[n+1:]

n = 3
print(rem_nth_idx(str, "G", n)) 