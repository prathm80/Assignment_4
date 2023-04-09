# Write a Python program to square the elements of a list using map() function.

# Sample List: [4, 5, 2, 9]

# Square the elements of the list:

# [16, 25, 4, 81]

def square(n):
    return n * n
num = [2, 3, 7, 8, 5]
print("original list:",num)
result = map(square, num)

print("square of list:",(list(result)))