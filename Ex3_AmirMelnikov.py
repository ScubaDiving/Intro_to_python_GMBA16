## Q1
# (c) Amir Melnikov GPL-3

import matplotlib.pyplot as plt
# Define a list with the following values; 10,20,32,54,67,-10,45,5,
my_list = [10, 20, 32, 54, 67, -10, 45, 5]

# Print the list.
print(my_list)

# Print the first element in the list.
print(my_list[0])

# Print the third element in the list.
print(my_list[2])

# Print the last element in the list.
print(my_list[-1])

# Print the elements in the even indices: (in entries 0,2,4,6,...).
print(my_list[::2])

# Print the sum of the list elements.
print(sum(my_list))

# Define an empty list.
empty_list = []

# Get the list size from the user to a variable named “length”.
length = int(input("Enter length of list: "))

# Get “length” elements from the user into the list.
for i in range(length):
    empty_list.append(int(input(f"Enter element {i+1}: ")))

# Print the list.
print(empty_list)

# Get an additional integer from the user.
new_int = int(input("Enter an integer to append to the list: "))

# Append the list (add the integer to the end of the list).
empty_list.append(new_int)

# Print the list.
print(empty_list)

# Delete the first element from the list.
del empty_list[0]

# Print the number of elements in the list (the list length).
print(len(empty_list))

# Get a value x from the user.
x = int(input("Enter a value x: "))

# Print the number of times that x appears in the list.
print(empty_list.count(x))

# Insert x to the list in entry 2 (as third element).
empty_list.insert(2,x)

# Print the list.
print(empty_list)

# Find the average of the list elements.
average = sum(empty_list)/len(empty_list)
print(average)

# Print the number of times x appears in the list.
print(empty_list.count(x))

## Q2

# Duplicate a list using extend.

# Given the list [1,2,3] the duplicated list will be: [1,2,3,1,2,3]
my_list = [1, 2, 3]
my_list.extend(my_list)
print(my_list)

## Q3
# Switch between the first and the last elements in a list.

# GIven the list: [1,2,3,4,5], the program will change it to: [5,2,3,4,1].
my_list = [1, 2, 3, 4, 5]
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)
## Q4
# Define a list and write a program that shifts all list elements one entry to the right and moves the last element to
# the first entry. Hint: you have to do that in 3 phases.

# Given the list: [1,2,3,4,5,6] the list will change to: [6,1,2,3,4,5] (It should be the same list,
# not a new list).
my_list = [1, 2, 3, 4, 5, 6]
last_element = my_list.pop()
my_list.insert(0,last_element)
print(my_list)

## Q4b
# Define a list and write a program that creates a new list that contains all elements of the given list, where all
# elements are shifted one entry to the left and the last element becomes the first element.

# Given the list: [1,2,3], the new list will be: [2,3,1].
my_list = [1, 2 ,3]
new_list = my_list[1:]
new_list.append(my_list[0])
print(new_list)

## Q5 - Data Visualization

# Create lists for weights and heights of both groups
weights_a = [80, 85, 90, 95, 100, 105, 110, 115]
weights_b = [70, 75, 80, 85, 90]
heights_a = [170, 172, 175, 178, 180, 182, 185, 188]
heights_b = [165, 168, 170, 173, 175]

# Create scatter plot
plt.scatter(weights_a + weights_b,
            heights_a + heights_b,
            c=['red']*len(weights_a) + ['blue']*len(weights_b),
            label=['Group A', 'Group B'])

# Add legend
plt.legend()

# Show plot
plt.show()