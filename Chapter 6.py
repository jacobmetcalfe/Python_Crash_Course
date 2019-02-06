# Chapter 6: Dictionaries
# Storing multiple data types in one piece of information
# This can be represented as an object or a dictionary
print('\n')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# A key value pair is a piece of a dictionary. Each key is connected to a value.
# A key value can be a number, string, list, or another dictionary
# A dictionary is wrapped in braces
# Can have an unlimited number of key values
new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')

# Adding New Key-Value Pairs
# Dictionaries are dynamic structures, it can be added to at any time
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# It is sometimes best to start with an empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Usually use empty dictionaries for user supplied data
# Modifying Values in a Dictionary
print('The alien is ' + alien_0['color'] + '.')
alien_0['color'] = 'yellow'
print('The alien is now ' + alien_0['color'] + '.')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))
alien_0['speed'] = 'fast'

# Removing Key-Value Pairs
del alien_0['x_position']
# Removes permanently

# A dictionary of Similar Objects
# This is how a dictionary should be laid out.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + '.')
print('\n')

# Exercises

# 6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age,
# and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.
person_I_know = {'first_name': 'JJ',
                 'last_name': 'perkins',
                 'age': 22,
                 'city': 'colorado springs'
                 }
print(person_I_know)

# 6-2. Favorite Numbers: Use a dictionary to store peopleís favorite numbers. Think of five names, and use them as
# keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary.
# Print each personís name and their favorite number. For even more fun, poll a few friends and get some actual data
# for your program.
print('\n')
favorite_numbers = {
    'roger': 15,
    'bill': 18,
    'nigel': 20,
    'sam': 22,
    'todd': 30
}
print("Roger's favorite number is " + str(favorite_numbers['roger']) + '.')
print("Bill's favorite number is " + str(favorite_numbers['bill']) + '.')
print("Nigel's favorite number is " + str(favorite_numbers['nigel']) + '.')
print("Sam's favorite number is " + str(favorite_numbers['sam']) + '.')
print("Todd's favorite number is " + str(favorite_numbers['todd']) + '.')
print('\n')

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion,
# lets call it a glossary. Think of five programming words you have learned about in the previous chapters. Use these
# words as the keys in your glossary, and store their meanings as values. Print each word and its meaning as neatly
# formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line
# and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between
# each word-meaning pair in your output.
glossary = {
    'list': 'list is a data structure in Python that is a mutable, '
            'or changeable, ordered sequence of elements',
    'integer': 'a whole number; a number that is not a fraction.',
    'double': 'The double is a fundamental data type built into the compiler and used to define numeric variables '
              'holding numbers with decimal points.',
    'range': 'The range() type returns an immutable sequence of numbers between the given start integer to the stop '
             'integer.',
    'immutable': 'cannot be changed'
}
print("List: " + glossary['list'] + '.\n')
print("Integer " + glossary['integer'] + '.\n')
print("Double: " + glossary['double'] + '.\n')
print("Range: " + glossary['range'] + '.\n')
print("Immutable: " + glossary['immutable'] + '.\n')

# Looping through all key-value pairs
# Does the exact same thing withut the keys method
for name in favorite_languages.keys():
    print(name.title())
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " +
              favorite_languages[name].title() + '!')

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!\n')

# Looping through a dictionary's Keys in Order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for taking our poll!')

# Looping through the values of a dictionary
# Checks all values without checking for repeats
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# The set method takes all repetitive values out, works for arrays too.
print("\nThe following unique languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
    print('\n')

# Examples 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (
# page 102) by replacing your series of print statements with a loop that runs through the dictionaryís keys and
# values. When youíre sure that your loop works, add five more Python terms to your glossary. When you run your
# program again, these new words and meanings should automatically be included in the output.
for term in glossary:
    print(term.title() + ': ' + glossary[term])

# 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value
# pair might be 'nile': 'egypt'. Use a loop to print a sentence about each river, such as The Nile runs through
# Egypt. Use a loop to print the name of each river included in the dictionary. Use a loop to print the name of each
# country included in the dictionary.
rivers = {
    'nile': 'egypt',
    'mississippi': 'the united states',
    'arkansas': 'the united states'
}
for river in rivers:
    print('The ' + river.title() + ' River runs through ' + rivers[river].title() + '.\n')

print('River: ')
for river in rivers.keys():
    print(river.title())
print('\n')
print('Country: ')
for river in rivers.values():
    print(river.title())

# 6-6. Polling: Use the code in favorite_languages.py (page 104). Make a list of people who should take the favorite
# languages poll. Include some names that are already in the dictionary and some that are not. Loop through the list
# of people who should take the poll. If they have already taken the poll, print a message thanking them for
# responding. If they have not yet taken the poll, print a message inviting them to take the poll.
favorite_languages = {'phil': 'python',
                      'sarah': 'c',
                      'jen': 'python',
                      'edward': 'ruby',
                      }
favorite_languages_2 = {'phil': 'python',
                        'sarah': 'c',
                        'jen': 'python',
                        'janet': 'c++',
                        }
for voter in favorite_languages:
    if voter in favorite_languages_2:
        print('Thanks for taking the poll: ' + voter.title())
    else:
        print('You should take our poll: ' + voter.title())
print('\n')
# Nesting
# Storing a set of dictionaries in a list
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# More intense example
# Make an empty list for storing the aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first five aliens
for alien in aliens[:5]:
    print(alien)
print('...')

print("Total number of aliens: " + str(len(aliens)))
print('\n')
# Lists inside of dictionaries
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese']
}
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print(topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}
for name, languages in favorite_languages.items():  # states 2 variables for loop, one for key, one for value
    print('\n' + name.title() + "'s favorite languages are:")
    for language in languages:
        print(language.title())

# Do not nest these too deeply, it makes it hard to read
# A Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {'first': 'marie',
               'last': 'curie',
               'location': 'paris'}
}
for username, user_info in users.items():
    print("\nUsername: " + username.title())
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("Full name: " + full_name.title())
    print("Location: " + location.title())

# Examples

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.
# Dictionaries 115
person_I_know = {'first_name': 'JJ',
                 'last_name': 'perkins',
                 'age': 22,
                 'city': 'colorado springs'
                 }
person_I_know2 = {'first_name': 'christopher',
                  'last_name': 'mccracken',
                  'age': 21,
                  'city': 'colorado springs'
                  }
person_I_know3 = {'first_name': 'jake',
                  'last_name': 'ridling',
                  'age': 20,
                  'city': 'colorado springs'
                  }
people = list([person_I_know, person_I_know2, person_I_know3])
for person in people:
    print(person['first_name'].title() + ' ' + person['last_name'].title() + ' is ' +
          str(person['age']) + ' and is from ' + person['city'].title())
    print('\n')

# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the ownerís
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.
rufus = {'type': 'dog',
         'owner_name': 'perkins'
         }
doug = {'type': 'hamster',
        'owner_name': 'bill'
        }
denny = {'type': 'fish',
         'owner_name': 'roger'
         }
pets = list([rufus, doug, denny])
for pet in pets:
    print('The ' + pet['type'] + ' is owned by ' + pet['owner_name'].title() + '.')
print('\n')

# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each personís name and their favorite places.
favorite_places = {'chris': ['atlanta', 'miami', 'washington'],
                   'jake': ['texas', 'detroit', 'the alamo'],
                   'jj': ['london', 'new york', 'denver'],
                   }
for name, places in favorite_places.items():
    print('\n' + name.title() + ' likes the following places: ')
    for place in places:
        print(place)
print('\n')
# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each persons
# name along with their favorite numbers.
favorite_numbers = {'chris': [1, 2, 3],
                    'jake': [5, 7, 9],
                    'jj': [18, 10, 14],
                    }
for name, numbers in favorite_numbers.items():
    print('\n' + name.title() + ' likes the following numbers: ')
    for number in numbers:
        print(number)
print('\n')

# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each cities dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.
cities = {
    'atlanta': {'country': 'united states',
                'population': 486290,
                'fact': "it is a city in Georgia",
                },
    'baltimore': {'country': 'united states',
                  'population': 611648,
                  'fact': "it is a city in Maryland",
                  },
    'dubai': {'country': 'united arab emirates',
              'population': 3137000,
              'fact': "it is a wealthy city",
              }
}
for city, facts in cities.items():
    print(city.title() + ' is in the ' + facts['country'].title() + ' with population '
          + str(facts['population']) + ' and ' + facts['fact'])
