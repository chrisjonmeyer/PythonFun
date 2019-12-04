# Create a generator that generates the squares of numbers up to some number N.

# def gensqaures(num):
#     for x in range(num):
#         yield x**2

# for y in gensqaures(10):
#     print(y)

# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# Note: Use the random library. For example:

# import random

# def rand_num(low,high,n):
#     for x in range(n):
#         yield(random.randint(low,high))

# for num in rand_num(1,10,12):
#     print(num)

# Use the iter() function to convert the string below into an iterator:
s = 'hello'

s_iter = iter(s)
print(next(s_iter))