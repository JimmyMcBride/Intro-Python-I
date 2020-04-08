# Python exposes a terse and intuitive syntax for performing 
# slicing on lists and strings. This makes it easy to reference
# only a portion of a list or string. 
# 
# This Stack Overflow answer provides a brief but thorough
# overview: https://stackoverflow.com/a/509295
# 
# Use Python's slice syntax to achieve the following:

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
one = a[1]
print(f"1) Correct answer: 4 | My answer: {one}")

# Output the second-to-last element: 9
two = a[-2]
print(f"2) Correct answer: 9 | My answer: {two}")

# Output the last three elements in the array: [7, 9, 6]
three = a[-3:]
print(f"3) Correct answer: [7, 9, 6] | My answer: {three}")

# Output the two middle elements in the array: [1, 7]
four = a[2:-2]
print(f"4) Correct answer: [1, 7] | My answer: {four}")

# Output every element except the first one: [4, 1, 7, 9, 6]
five = a[1:]
print(f"5) Correct answer: [4, 1, 7, 9, 6] | My answer: {five}")

# Output every element except the last one: [2, 4, 1, 7, 9]
six = a[:-1]
print(f"6) Correct answer: 4 | My answer: {six}")

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
seven = s[7:12]
print(f"7) Correct answer: 'world' | My answer: '{seven}'")
