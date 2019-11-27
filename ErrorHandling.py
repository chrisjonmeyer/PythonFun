# Error Handling

# for i in ['a','b','c']:
#     try:
#         print(i **2)
#     except:
#         print( i + " is a string, not an int!")

# x = 5
# y = 0
# try:
#     z = x/y
# except:
#     print("This function does not work")
# finally:
#     print("All done")

def ask():
    while True:
        try:
            value = int(input("Please enter a number:"))
        except:
            print("You did not enter a number.")
            continue
        else:
            break
    print("Thank you, your number squared is: ", value**2)
ask()
