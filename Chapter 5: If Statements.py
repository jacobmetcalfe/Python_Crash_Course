# Chapter 5: If Statements
print('\n')
cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# Bases the if statement off of booleans of true and false, looks to see if value is bmw and if it is then it is
# considered true, if it isn't then it is false
# Capitalization is not considered so 'audi' is not equal 'Audi'
# Would need to use .lower() function
# Website username are converted to lowercase to make sure no one else has the same username
print('\n')
# Checking for Inequalities
requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print('Hold the anchovies!')

print('\n')
# Can do the same with numerical expressions age == 18
answer = 17
if answer != 17:
    print('That is not the correct answer')

# Other math expressions can be used
age = 19
if age <= 19:
    print('You are young')

# Multiple Expressions
age_0 = 22
age_1 = 18
if (age_0 == 22) and (age_1 == 18):
    print('You two are four years apart!')
# Should use parentheses with multiple expressions to improve readability
# You can also use or to check if one or the other conditions are true
if age_0 or age_1 == 22:
    print('One of you is 22 years old.')

# Check whether a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print('You like mushrooms on pizza?!')

# Checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + " you are not in the banned user list.")

# Boolean values are either true and false

# Examples 5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and
# your prediction for the results of each test. Your code should look something like this: car = 'subaru' print("Is
# car == 'subaru'? I predict True.") print(car == 'subaru') print("\nIs car == 'audi'? I predict False.") print(car
# == 'audi') Look closely at your results, and make sure you understand why each line evaluates to True or False.
# Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.
print('\n')
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print(car != 'audi')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print(car == 'Subaru')
print(car != 'subaru')

# 5-2. More Conditional Tests: You do not have to limit the number of tests you create to 10. If you want to try more
# comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for
# each of the following: Tests for equality and inequality with strings Tests using the lower() function Numerical
# tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or
# equal to Tests using the and keyword and the or keyword Test whether an item is in a list Test whether an item is
# not in a list
print('\nTest for strings:')
string1 = 'Hi'
string2 = 'Hi'
string3 = "hi"
if string1 == string2:
    print('The strings are equal')
if string2 != string3:
    print('The strings are not equal')
if string2.lower() == string3.lower():
    print('The lowercase strings are the same')
print('\nTest for numbers:')
num1 = 5
num2 = 5
num3 = 6
if num1 == num2:
    print('The numbers are equal')
if num2 != num3:
    print('The numbers are not equal')
if num3 > num2:
    print("The third number is greater than the second")
if num2 < num3:
    print("The second number is less than the third")
if num2 <= num1:
    print("The second number is less than or equal to the first")
if num1 >= num2:
    print('The first number is greater than the second')
if num1 and num2 == '5':
    print('The two numbers equal 5')
if num1 or num2 == '6':
    print('One of the two numbers equals six')
if 'audi' in cars:
    print("Audi is in the list 'cars'")
if 'ferrari' not in cars:
    print("Ferrari is not in the list 'cars'")
print('\n')

# If-else statements
# If one thing is not the case, then do this other thing
age = 17
if age == 18:
    print('You can vote!')
else:
    print("You can't vote yet, sorry.")

# The way the statement chain goes is if-elif-else
# elif is else if, basically another if statement before all else
# Can adjust variables as well as shown in the bottom statement
age = 12
if age < 4:
    print('Your admission cost is free')
    price = 0
elif 4 < age < 18:
    print('Your admission cost is $5')
    price = 5
elif age == 18:
    print('Your admission costs $7.50')
    price = 7.50
else:
    print('Your admission cost is $10')
    price = 10

print('Your admission cost is $' + str(price) + '.')

# Python does not require an else statement however it is highly recommended you have a backup plan.
# Sometimes multiple if statements are necessary, because it will skip the rest, just in case two statements are true.
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'onions' in requested_toppings:
    print('Adding onions')
print('Finished making the pizza!')

# 5-3. Alien Colors 1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign
# it a value of 'green', 'yellow', or 'red'. Write an if statement to test whether the aliens color is green. If it
# is, print a message that the player just earned 5 points. Write one version of this program that passes the if test
# and another that fails. (The version that fails will have no output.)
print('\n')
alien_color = 'red'
if alien_color == 'green':
    print('Congrats, you earned five points')
if alien_color == 'red':
    print('Congrats, you earned five points!')

# 5-4. Alien Colors 2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain. If the
# aliens color is green, print a statement that the player just earned 5 points for shooting the alien. If the
# aliens color is not green, print a statement that the player just earned 10 points. Write one version of this
# program that runs the if block and another that runs the else block.
if alien_color == 'green':
    print('Congrats, you earned five points')
else:
    print('Congrats, you got 10 points!')
# 5-5. Alien Colors 3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain. ï If the alien is green,
# print a message that the player earned 5 points. If the alien is yellow, print a message that the player earned 10
# points. If the alien is red, print a message that the player earned 15 points. Write three versions of this
# program, making sure each message is printed for the appropriate color alien.
if alien_color == 'green':
    print('Congrats, you earned five points')
elif alien_color == 'yellow':
    print('You earned 10 points!')
else:
    print('You earned 15 points')
# 5-6. Stages of Life: Write an if-elif-else chain that determines a persons stage of life. Set a value for the
# variable age, and then: If the person is less than 2 years old, print a message that the person is a baby. the
# person is at least 2 years old but less than 4, print a message that the person is a toddler. If the person is at
# least 4 years old but less than 13, print a message that the person is a kid. If the person is at least 13 years
# old but less than 20, print a message that the person is a teenager. If the person is at least 20 years old but
# less than 65, print a message that the person is an adult. If the person is age 65 or older, print a message that
# the person is an elder.
age = 5
if age < 2:
    print('You are a baby.')
elif 2 < age < 4:
    print('You are a toddler.')
elif 4 < age < 13:
    print('You are a kid.')
elif 13 < age < 20:
    print('You are a teenager.')
elif 20 < age < 65:
    print('You are an adult.')
else:
    print('You are an elder.')
# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that
# check for certain fruits in your list. Make a list of your three favorite fruits and call it favorite_fruits. Write
# five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your
# list, the if block should print a statement, such as You really like bananas!
favorite_fruits = ['strawberry', 'banana', 'orange', 'grape', 'watermelon']
print('\n')
if 'strawberry' in favorite_fruits:
    print('I love Strawberries!')
if 'kiwi' in favorite_fruits:
    print('I love kiwi!')
if 'banana' in favorite_fruits:
    print('I love bananas!')
if 'orange' in favorite_fruits:
    print('I love strawberries!')
if 'grape' in favorite_fruits:
    print('I love grapes!')
if 'watermelon' in favorite_fruits:
    print('I love watermelon!')
print('\n')
# Using if statements with lists
# Checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('We are out of green peppers.')
    else:
        print('Adding ' + requested_topping)
print('These are your requested toppings')

# Checking that list is not empty
# if requested_toppings:  checks if list is empty or not
print('\n')
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding' + requested_topping)
    print('Pizzas done!')
else:
    print('Your pizza will be plain.')

# Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping)
    else:
        print('Sorry we cannot put ' + requested_topping + ' on this pizza.')

# 5-8. Hello Admin: Make a list of five or more user names, including the name 'admin'. Imagine you are writing code
# that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting
# to each user: If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a
# status report? Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.
users = ['admin', 'rodger', 'fanny', 'aaron', 'phillip']
for user in users:
    if 'admin' == user:
        print('Hello admin, would you like to see a status report?')
    else:
        print("Hello " + user.title())

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty. If the list is empty,
# print the message We need to find some users! Remove all of the usernames from your list, and make sure the correct
# message is printed.
print('\n')
users = []
if users:
    print("Hello users!")
else:
    print("We need to find some users!")

# 5-10. Checking User names: Do the following to create a program that simulates how websites ensure that everyone has
# a unique username. Make a list of five or more use names called current_users. Make another list of five user names
# called new_users. Make sure one or two of the new user  names are also in the current_users list. Loop through the
# new_users list to see if each new username has already been used. If it has, print a message that the person will
# need to enter a new username. If a username has not been used, print a message saying that the username is
# available. Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.
current_users = ['admin', 'rodger', 'fanny', 'aaron', 'phillip']
new_users = ['jacob', 'johnny', 'harry', 'aaron', 'phillip']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user.title() + ': Username taken, you will need a new one.')
    else:
        print(new_user.title() + ': Username is available.')

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers
# end in th, except 1, 2, and 3. Store the numbers 1 through 9 in a list. Loop through the list. Use an if-elif-else
# chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th
# 5th 6th 7th 8th 9th", and each result should be on a separate line.
ordinals = list(range(1, 10))
for ordinal in ordinals:
    if ordinal == 1:
        print(str(ordinal) + 'st')
    elif ordinal == 2:
        print(str(ordinal) + 'nd')
    elif ordinal == 3:
        print(str(ordinal) + 'rd')
    elif 10 > ordinal > 3:
        print(str(ordinal) + 'th')

# Styling if statements
# Always do
# if age < 4:
# Rather than
# if age<4

# I already do exercises in above work.
