# Custom  range function

def Range(start=0,stop=0,step=1):
    '''
    Mimics the built-in range function.
    
    Parameters:
        start (int,optional): The starting number of the range. Defaults to 0.
        stop (int): The ending number of the range.Stopping value (non-inclusive).
        step (int, optional): The step size default is 1.
    
    Returns:
        generator: A generator yielding values from start to stop(non-inclusive)
    '''
    if step == 0:
        raise ValueError("Step cannot be zero.")
    if step > 0:
        current = start
        while current < stop:
            yield current
            current += step
    elif step < 0:
        current = start
        while current > stop:
            yield current
            current += step
            

# Example usage

for num in Range(1,11):
    print(num,end=" ")
print()
for num in Range(1,11,2):
    print(num,end=" ")
print()
for num in Range(0,-10,-1):
    print(num,end=" ")
print()
for num in Range(0,-10,-3):
    print(num,end=" ")
print()
