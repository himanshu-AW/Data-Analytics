# 4. Write a Python program to construct the following pattern, using a nested forloop.  
# *  
# * *   
# * * *   
# * * * *   
# * * * * *   
# * * * *   
# * * *   
# * *   
# *  

def print_pattern(n):
    m=n*2
    for i in range(1,m):
        for j in range(1,m):
            if (( i<=m/2 and j<=m/2 and i>=j) or (i>=m/2 and i+j<=m and j<=m/2)):
                print("* ",end="")
        print()
        
print_pattern(5)