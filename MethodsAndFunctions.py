# GitHub Practice Test:
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        else: 
            return a
    else:
        if a > b:
            return a
        else: 
            return b

print(lesser_of_two_evens(2,4))

