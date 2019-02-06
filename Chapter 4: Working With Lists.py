# Chapter 4: Working With Lists

# Looping through a list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
# Defines magician as part of magicians and prints each magician for each iteration of the list until the list is done

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
# Every indented line following is considered part of the loop

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# Summarizes the solution
print("Thanks for showing your tricks guys!")

# If you don't indent then you will get an error
# Example
# for magician in magicians
# print(magician)

# This is a syntax error
# A logical error gives a result, however it is not the desired result.
# Syntax errors are easy to resolve, logical errors can take a long time to resolve
# You can also indent when unnecessary producing unexpected indent error
# If you forget to indent, that would be a logical error
# If you forget the colon at the end of the first line of the loop you will get a syntax error

# Examples 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list,
# and then use a for loop to print the name of each pizza. Modify your for loop to print a sentence using the name of
# the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output
# containing a simple statement like I like pepperoni pizza. Add a line at the end of your program, outside the for
# loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of
# pizza you like and then an additional sentence, such as I really love pizza!
pizzas = ['pepperoni', 'pineapple', 'sausage']
for pizza in pizzas:
    print('I love ' + pizza + ' pizza.')
print('I like pizza!\n')

# 4-2. Animals: Think of at least three
# different animals that have a common characteristic. Store the names of these animals in a list, and then use a for
# loop to print out the name of each animal. Modify your program to print a statement about each animal,
# such as A dog would make a great pet. Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would make a great pet!
animals = ['fish', 'gorilla', 'human']
for animal in animals:
    print('A ' + animal + ' would make a great pet!')
print('All of these animals have eyes!\n')

# Numerical Lists
# The range function
for value in range(1, 5):
    print(value)
# Does not print the final number of the range

# list() and range() function
# Creates a list with that range of numbers in it.
numbers = list(range(1, 6))
print(numbers)

# The range function can skip numbers too
even_numbers = list(range(2, 11, 2))
print(even_numbers)
# Tells the program to make a list of the numbers 2-10 and to do every two numbers

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
# Makes an empty array, takes the number of value squared and adds it to the original squares array.

# To make it much easier we could just do it in one line
squares2 = []
for value in range(1, 11):
    squares2.append(value ** 2)
print(squares2)

# Simple statistics can be done with lists as well
# Min function
print(min(squares))

# Max function
print(max(squares))

# Sum function
print(sum(squares))

# List comprehension combines everything in one line
squares = [value ** 2 for value in range(2, 11)]
print(squares)
print('\n')

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for value in range(1, 21):
    print(value)
print('\n')

# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
# (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)
# Would ruin code if I ran it
million = list(range(1, 1000001))
# print(million)

# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make
# sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly
# Python can add a million numbers.
print(min(million))
print(max(million))
print(sum(million))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
# Use a for loop to print each number.
odds = list(range(1, 21, 2))
print(odds)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
three_multiples = list(range(3, 31, 3))
for three_multiple in three_multiples:
    print(three_multiple)
print("\n")
# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in
# Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop
# to print out the value of each cube.
cubes = []
for value in range(1, 11):
    cubes.append(value ** 3)
for cube in cubes:
    print(cube)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
cube_comp = [value ** 3 for value in range(1, 11)]
print(cube_comp)

# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# Prints the list of players from index 0 to 2, similar to the range function

print(players[1:4])
# Prints index of players 1-5 of the array.

print(players[2:])
# Prints players starting at index 2 and goes to the end of the list.

print(players[-3:])
# Does the same thing except starts from the 3rd to last of array

# Looping through a slice
print('Here is a list of players on my team:')
for player in players[:3]:
    print(player.title())

# Copying a list
# Can copy a list by omitting the first index and the second index ([:])
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]
print("My favorite foods are:")
my_foods.append('ice cream')
print(my_foods)
print("My friends favorite foods are:")
friends_foods.append('cannoli')
print(friends_foods)
print('\n')

# This does not work my_foods = friends_foods
# This will make both variables point to the same list.
# For now, make sure that you are copying using slice rather than pointing

# Examples 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the
# program that do the following: Print the message, The first three items in the list are:. Then use a slice to print
# the first three items from that programs list. Print the message, Three items from the middle of the list are:.
# Use a slice to print three items from the middle of the list. Print the message, The last three items in the list
# are:. Use a slice to print the last three items in the list.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('The first three items in the list are:')
print(cars[0:3])
print('\n The next few items in the list are:')
print(cars[2:4])
print('\n The final item is:')
print(cars[3:5])
print('\n')
# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 60). Make a copy of the list of
# pizzas, and call it friend_pizzas. Then, do the following: Add a new pizza to the original list. Add a different
# pizza to the list friend_pizzas. Prove that you have two separate lists. Print the message, My favorit epizzas
# are:, and then use a for loop to print the first list. Print the message, My friendís favorite pizzas are:,
# and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
friends_pizzas = pizzas[:]
friends_pizzas.append('salami')
pizzas.append('oregano')
print('My favorite Pizzas are: ')
print(pizzas)
print('\nMy friends favorite pizzas are: ')
print(friends_pizzas)
print('\n')

# 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing to save
# space. Choose a version of foods.py, and write two for loops to print each list of foods.
for my_food in my_foods:
    print(my_food)
print('\n')
for friends_food in friends_foods:
    print(friends_food)
print('\n')

# Tuples
# A tuple is a list that cannot be changed, making it immutable
# A tuple looks similar except you use parentheses instead
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 201 cannot change because its a tuple
# print(dimensions[0]) gives error

# For loop through
for dimension in dimensions:
    print(dimension)

# How to change tuples
dimensions = (400, 200)
for dimension in dimensions:
    print(dimension)
print('\n')
# Examples
# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods,
# and store them in a tuple. Use a for loop to print each food the restaurant offers. Try to modify one of the items,
# and make sure that Python rejects the change. The restaurant changes its menu, replacing two of the items with
# different foods. Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on
# the revised menu.
buffet_foods = ('pizza', 'sushi', 'crab legs', 'rice')
print("The original menu is:")
for buffet_food in buffet_foods:
    print(buffet_food)
# buffet_foods[0] = 'jerky'

print('\nThe new menu is:')
buffet_foods = ('lo mein', 'lasagna', 'crab legs', 'rice')
for buffet_food in buffet_foods:
    print(buffet_food)

# Styling your code
# Write neat code
# The Style Guide
# When someone wants to make a change to the Python language, they write a Python Enhancement Proposal(PEP)
# Basically just said write neat code, in which if you have a good IDE it should do anyways
# If not, make sure you include blank lines, four lines per indentation, and 80 characters per line.
