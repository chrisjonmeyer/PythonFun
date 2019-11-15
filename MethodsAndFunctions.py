# GitHub Practice Test:
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
# def lesser_of_two_evens(a,b):
#     if a % 2 == 0 and b % 2 == 0:
#         if a > b:
#             return b
#         else: 
#             return a
#     else:
#         if a > b:
#             return a
#         else: 
#             return b

# print(lesser_of_two_evens(2,4))

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

# def old_macdonald(name):
#     if len(name) > 3:
#         first_name = name[:3]
#         second_name = name[3:]
#         first_name = first_name.capitalize()
#         second_name = second_name.capitalize()
#         full_name = first_name + second_name
#     else:
#         full_name = name.capitalize()
#     return full_name

# print(old_macdonald('chris'))

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

# def almost_there(n):
#     if n < 100 and 100 - n < 10:
#         return True
#     elif n > 100 and n < 110:
#         return True
#     elif n > 100 and n < 200 and 200 - n < 10:
#         return True
#     elif n > 200 and n < 210:
#         return True
#     else:
#         return False

# print(almost_there(93))
# print(almost_there(104))
# print(almost_there(150))
# print(almost_there(209))

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# def has_33(nums):
#     for n in range(0, len(nums) -1):
#         if nums[n] == 3 and nums[n+1] == 3:
#             return True
#     return False
            

# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# def blackjack(a,b,c):
#     total_val = a+b+c
#     if total_val == 21:
#         return 'BLACKJACK'
#     elif total_val < 21:
#         return total_val
#     elif total_val > 21 and a == 11 or b == 1 or c == 11:
#         return total_val - 10
#     else:
#         return 'BUST'

# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9,9,11))
# print(blackjack(7,6,8))

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in orde

def spy_game(nums):
    for n in range(0, len(nums) -2):
        if nums[n] == 0 and nums[n+1] == 0 and nums[n+2] == 7:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,2,4,4,0,7,5]))
print(spy_game([1,2,4,0,2,7,5]))