# Using this test functions for practice.

# def first_function():
#     '''
#     DOCSTRING: This is your commet area for the function
#     '''
#     print("Hello")

# first_function()


# Create a function that takes an arbitrary number of arguments and returns a list containing
# only the arguments that are even
def myfunc(*args):
    evens = []
    for x in args:
        if x % 2 == 0:
            evens.append(x)
    return evens

value = myfunc(1,2,3,4,5,6,7,8)
print (value)