# Chapter 8: Functions
# Functions are blocks of code that are designed to do one specific job
# Always want to pass information to functions

# Defining a function
def greet_user():  # function definition
    print('Hello')


greet_user()  # Will print 'hello' due to the method being called.


# Passing information to a function
def greet_user(username):
    print('Hello ' + username.title() + '!')


greet_user('Jesse')  # passing jesse in as a username, for it to later print out


# You can call greet_user() as many times as you want and pass it any name

# Arguments and Parameters
# Username acted as a parameter, a piece of information the function needs to do its job
# The specific thing you passed 'jesse' is known as an argument and stored as the username

# Examples
# 8-1. Message: Write a function called display_message() that prints one sentence
# telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.
def display_message():
    print('We are learning about functions in this chapter.')


display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.
print('\n')


def favorite_book(title):
    print('Your favorite book is: ' + title.title())


favorite_book('Alice in Wonderland')

# NOTE: 2 Blank lines expected after defining functions

# Passing Arguments
# Python has to match the value that you pass into it calling them positional arguments
print('\n')


def describe_pet(animal_type, pet_name):
    print('I have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title())


# Goes into the function respectively (in order) hamster = animal_type
describe_pet('hamster', 'harry')
print('\n')
# Multiple function calls, just describes different dog, put different arguments
describe_pet('dog', 'willie')
print('\n')
# Will go in as wrong variables due to it being left to right
describe_pet('harry', 'hamster')
print('\n')

# Keyword Arguments
# A keyword argument is a name-value pair that you pass into a function
# This makes it so order no longer will matter
describe_pet(animal_type='hamster', pet_name='harry')
# OR
describe_pet(pet_name='harry', animal_type='hamster')
# Will print the same thing because we are explicitly calling on each parameter
print('\n')


# Default Values
# Defines the type as a dog, non default values must be placed first as parameters as that is how Python interprets them
def describe_pet(pet_name, animal_type='dog', ):
    print('I have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title())


# Willie is a dog, dog was already defined, we are just passing willie in
describe_pet(pet_name='willie')
print('\n')
# You can still change the animal type if you use it explicitly again
describe_pet(pet_name='roger', animal_type='turtle')


# Equivalent function calls
# Functions can have many equivalent calls
# NOTE: Doesn't matter which calling stile you use, as long as it is easy to read and produces the correct output

# Avoiding Argument Errors
# could not just do
# describe_pet()
# you are not passing any arguments in and python does not know what to put for those values
# Will get the error 'TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
# Will get a similar error when you do too many arguments

# Examples
# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.
def make_shirt(size, text):
    print('Your size ' + size + " shirt says '" + text + "' on the front")


make_shirt('M', "What's up")
make_shirt(text='Hi', size='L')

print('\n')


# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.
def make_shirt(size, text):
    if size == 'L':
        print('Your size ' + size + " shirt says 'I love Python' on the front")
    else:
        print('Your size ' + size + " shirt says '" + text + "' on the front")


make_shirt('M', "What's up")
make_shirt(text='Hi', size='L')
print('\n')


# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.
def describe_city(city, country='italy'):
    print(city.title() + ' is in ' + country.title())


describe_city('venice')
describe_city('naples')
describe_city('new york city', country='the united states')

# Return Values
