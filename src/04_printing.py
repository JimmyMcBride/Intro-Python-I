# Python provides a number of ways to perform printing. Research
# how to print using the printf operator, the `format` string
# method, and by using f-strings.

x = 10
y = 2.204623
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x, y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

# Use the 'format' string method to print the same thing

# Finally, print the same thing using an f-string
print("There are %flbs in 1kg" % y)
print("If you give me ${0} right now, I'll give you ${1} later.".format(y, x))
print(f"{z} I'll take {x}.")

# Notes:
# You can call numbers and floats strings, but you can not call strings numbers or floats.
