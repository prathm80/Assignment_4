# Write a Python program to triple all numbers of a given list of integers. Use Python map.

# sample list: [1, 2, 3, 4, 5, 6, 7]

# Triple of list numbers:

# [3, 6, 9, 12, 15, 18, 21]

list1 = [1, 3, 5, 6, 2, 8, 6]
print("original list of numbers:",list1)
triple_of_numbers = map(lambda x  : x+x+x, list1)
print("triple of numbers:")
print(list(triple_of_numbers))