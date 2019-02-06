# Chapter 7: User input and while loops
# Most programs solve an end user's problem
# Need user input to do so

# Simple input statement
# defining message as variable to store input, after input is just the message that you want to display
# will store in message until 'enter' is pressed
print('\n')
message = input("Tell me something and I will repeat it back to you: ")
# prints what you typed
print(message)

name = input("Please enter you name: ")
print("Hello " + name + '!')

# Make a long prompt message
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is you first name?"
name = input(prompt)
print("Hello " + name + '!')

# Cannot store integers the same way, such as if I entered 18, 18 would be a string not an int
# So, we have to explicitly cast it into an int
age = input('How old are you?')
age = int(age)  # casting
if age >= 18:
    print('You can vote!')
else:
    print('You are young!')

# The Modulo operator
# The Modulo operator returns the remainder
print(4 % 3)  # Equal to 1 because 3 goes into 4, 1 R 1 times
print(5 % 3)  # Equal to 2 because 3 goes into 5, 1 R 2 times
print(6 % 3)  # Equal to 0 because 3 goes into 6 exactly 2 times

# One thing we can do with this is check divisibility
number = input("Enter a number, and I'll tell you if it is even or odd:")
number = int(number)
if number % 2 == 0:
    print(str(number) + ' is even')
else:
    print(str(number) + ' is odd')

# Output in Python 2.7
# In Python 2.7, raw_input() is used because Python attempts to interpret it and it could convert it to the wrong data
# type, causing miscalculations

# Examples

# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as ìLet me see if I can find you
# a Subaru.î
rental_car = input('What kind of rental car would you like? ')
print('Let me see if I can find you a ' + rental_car)

# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# theyíll have to wait for a table. Otherwise, report that their table is ready.
dinner_group = input('How many people are in your dinner group?')
dinner_group = int(dinner_group)
if dinner_group > 8:
    print('You will have to wait for a table')
else:
    print('Your food is ready')

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.
number = input('Enter a number and I can tell you if it is divisible by ten or not')
number = int(number)
if number % 10 == 0:
    print(str(number) + ' is divisible by ten')
else:
    print(str(number) + ' is not divisible by 10')
print('\n')

# Introducing while loops
# simple while loop to count from 1 to 5, loop will not stop until it reaches the while value
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Letting the User Choose when to quit
prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program. "  # prompt
message = ''  # place holder for while loop
while message != 'quit':  # as long as user doesn't say 'quit' keep the loop going
    message = input(prompt)  # input

if message != 'quit':  # only prints message as long as it is not equal to quit.
    print(message)  # print

# Using a flag
# A flag is like a signal to the program
# The flag will equal true to keep the program running, but will equal false when it needs to end

# In the following program, once 'quit' is typed the active signal will go to false, causing the while loop to end
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# Using break to exit a loop
prompt = "\nPlease enter the name of a city you have visitied:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:  # while the program doesn't break
    city = input(prompt)
    if city == 'quit':
        break  # will stop the while loop, making it false
    else:
        print("I'd love to go to " + city.title())

# Using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # will back to the top of the while loop and start it again until an odd number shows

    print(current_number)  # will print only the odd numbers

# Avoiding infinite loops
# This loop runs forever, only printing 1
# x = 1
# while x <= 5:
#    print(x)
# Will only print 1's because nothing is incrementing x, meaning it will never hit 5, always continuing the loop
# How to avoid
# Test every while loop and make sure the loop stops when you expect it to
# Run as many cases as you can to make sure someone cannot break your program

# Examples
# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying youíll add that topping to their pizza.

prompt = "Enter what kind of toppings you want: (Enter 'quit' to stop entering)"
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(topping + ' was added to the pizza.')


# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person's age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

ticket_total = 0
while True:
    age_prompt = "How old is the guest? (Type 'quit' to quit)"
    age = input(age_prompt)
    if age == 'quit':
        break
    elif int(age) < 3:
        ticket_price = 0
    elif 3 < int(age) < 12:
        ticket_price = 10
    else:
        ticket_price = 15
    ticket_total += ticket_price
print('Your total ticket price $' + str(ticket_total))

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# Use a conditional test in the while statement to stop the loop.
# Use an active variable to control how long the loop runs.
# Use a break statement to exit the loop when the user enters a 'quit' value.
print('\n')

# First Loop
x = 0
while x < 5:
    print(x)
    x += 1

print('\n')
# Second Loop
x = 0
active = True
while active:
    if x < 5:
        print(x)
        x += 1
    else:
        active = False
print('\n')

# Third Loop
x = 0
while True:
    if x < 5:
        print(x)
        x +=1
    else:
        break

# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
# ctrl-C or close the window displaying the output.)
# I will not really run, because that would ruin the previous code
# x = 1
# while x > -1:
#     print(x)
#     x += 1

# Second Part of Chapter 7
# Should not modify a list inside a for loop because Python will not be able to keep track of values
# To modify a list as you work through it use while loops

# Moving items from one list to another

# List that needs to be verified and an empty list to hold confirmed users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users
print('The confirmed users are: ')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# Will print in opposite order due to the pop method getting the top value of the list/ the last value added to the
# array

# Removing all instances of specific values from a list
# Originally the 'remove' function only removed one value from the list at a time, this loop will remove all
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

# loop to remove all 'cat' strings in the array
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# Filling a dictionary with user input
responses = {}
polling_active = True
while polling_active:
    # Prompt for the person's name and response
    name = input('\nWhat is your name? ')
    response = input('Which mountain would you like to climb someday? ')

    # Store the response in a dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input('Would you like to let another person respond?(yes/no)')
    if repeat == 'no':
        polling_active = False
for name, response in responses.items():
    print((name.title() + ' would like to climb ' + response.title() + '.'))

# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.
sandwich_orders = ['club', 'turkey', 'ham', 'roast beef']
finished_sandwiches = []
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print('Preparing: ' + finished_sandwich)
    finished_sandwiches.append(finished_sandwich)

for sandwich in finished_sandwiches:
    print('Your ' + sandwich + ' is all done.')

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.
sandwich_orders = ['club', 'turkey', 'ham', 'roast beef', 'pastrami', 'pastrami', 'pastrami']
print('The deli has run out of Pastrami')
while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
print(sandwich_orders)

# 7-10. Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.
vacations = {}
vacations_poll = True
while vacations_poll:
    name = input('What is your name?')
    vacation = input('What is your dream vacation?')
    vacations[name] = vacation
    repeat = input('Would you like to let another person respond?(yes/no)')
    if repeat == 'no':
        vacations_poll = False

for name, vacation in vacations.items():
    print((name.title() + "'s dream vacation is " + vacation.title() + '.'))
