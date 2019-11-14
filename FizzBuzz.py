# This prints out Fizz for every number that is divisible by 3. Buzz for every number
# divisble by 5. And FizzBuzz for every number divisible by 3 and 5.
number = 0

while number < 100:
    number += 1
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else: 
        print(number)
