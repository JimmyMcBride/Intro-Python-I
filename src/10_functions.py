# Write a function is_even that will return true if the passed-in number is even.

def is_even_steven(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# A comment

# Print out "Even!" if the number is even. Otherwise print "Odd"

if is_even_steven(num):
    print("Is even Steven!!!")
else:
    print("Is not even Steven. :(")

