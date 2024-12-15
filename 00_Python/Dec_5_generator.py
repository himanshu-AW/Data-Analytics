def mygen(n):
    """This is a generator function that yields numbers in a sequence"""
    c = 1
    print("start executing")
    while n:
        # print(f"{c} extcuted")
        # yield c
        c += 1
        n-=1
        # print("n value : ",n)
        # yield c
        return c
    
# Call the generator function and print the values
# natural = mygen(5)
c=4
while c>0:
    natural = mygen(5)
    try:
        # print(next(natural))
        print(natural)
        c-=1
    except StopIteration:
        break

# for i in natural:
#     print(i)

# for i in natural:
    # print(i)
    # print(next(natural))
    # print(next(i))


# def func(i):
#     print("excuted")
#     print(i)

# for i in range(4):
#     func(i)