# creating lists
numbered_list = [2, 4, 6, 8, 9, 0, 3, 5, 6]
text_list = ['apple', 'oranges', 'mangoes', 'x', 'y', 'z']
mixed_list = [45, 'This is the second element', 2019, [56, 34, 'xyz']]

# Displaying Lengths
print(len(numbered_list))
print(len(text_list))
print(len(mixed_list))
print(len(mixed_list[3]))

# Accessing Values
print(numbered_list[4:6])
print(text_list[:1])
if 4 in numbered_list:
    print(mixed_list[3][2])
elif 8 in numbered_list:
    print(mixed_list[1])
else:
    print(mixed_list[3])

# Adding new elements into the list
print(numbered_list)
numbered_list = numbered_list + [33, 55, 10]
print(numbered_list)
numbered_list.append(89)
print(numbered_list)
numbered_list.insert(4, 46)
print(numbered_list)

# Deleting items from list
del(numbered_list[4])
print(numbered_list)
del(numbered_list[9:])
print(numbered_list)

# Updating Lists
numbered_list[4] = 7
numbered_list[5:7] = [0, 2, 4, 5]
print(numbered_list)

# Doubling the elements in the list
for num in numbered_list:
    num = num * 2
print(numbered_list)

for i in range(len(numbered_list)):
    numbered_list[i] = numbered_list[i] * 2
print(numbered_list)

# List Comprehensions
squared_numbers = [n**2 for n in numbered_list]
print(squared_numbers)



