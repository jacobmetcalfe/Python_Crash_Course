# Chapter 3, Lists
# A list is a collection of items in a particular order
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# Prints entire list
print(bicycles)

# Access individual items of a list
print(bicycles[0]) # Prints 1st item

# Make it a clean format, title first word
print(bicycles[0].title())

# Index Postions start at 0, not 1, first item of a list is the 0th position
print(bicycles[1].title())

# Can index backwards in a list as well
print(bicycles[-1].title())
bike_msg = "My first bicycle was a " + bicycles[0].title() + "."
print(bike_msg + "\n")

# Exercises

# 3-1. Names: Store the names of a few of your friends in a list called names. Print each personís name by accessing
# each element in the list, one at a time.
friends_list = ["JJ", "Jake", "Chris"]
print(friends_list[0])
print(friends_list[1])
print(friends_list[2])
print("\n")

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each personís name,
# print a message to them. The text of each message should be the same, but each message should be personalized with
# the personís name.
friends_greeting = "Hey, how are you "
print(friends_greeting + friends_list[0])
print(friends_greeting + friends_list[1])
print(friends_greeting + friends_list[2])

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list
# that stores several examples. Use your list to print a series of statements about these items, such as ìI would
# like to own a Honda motorcycle.î
transportation_msg = "I would like to own a "
type_of_vehicle = " motorcycle"
brand_names = ["Honda", "Suzuki", "Daytona"]
print(transportation_msg + brand_names[0] + type_of_vehicle)
print(transportation_msg + brand_names[1] + type_of_vehicle)
print(transportation_msg + brand_names[2] + type_of_vehicle)

# Changing, Adding, and Removing Elements
# Changing Elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding Elements
# Append adds to the end of the list.
motorcycles.append('honda')
print(motorcycles)

# Inserting Data
motorcycles.insert(0, 'harley')  # inserts at 0th position
print(motorcycles)

# Deleting Data
del motorcycles[0]
print(motorcycles)

# Pop method removes the last item in a list, but it lets you work with the item after removing it., top of a stack
# is the end of a list
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".\n")

# Will pop the item in the 0th position
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.\n')

# Each time pop is used, the item is no longer in the list If you want to delete an item from a list and not use that
# item in any way use del, if you see future use with the item use pop

# Removing an item by Value
motorcycles.remove('yamaha')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print("\nA " + too_expensive.title() + " is too expensive for me.\n")
# The remove method only deletes one occurence of the action, if there are multiple of the same then a loop must be used

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that
# includes at least three people youíd like to invite to dinner. Then use your list to print a message to each
# person, inviting them to dinner.
guest_list = ['Gerald', 'Gerard', 'Richard']
print(guest_list[0] + " please come to my dinner.")
print(guest_list[1] + " please come to my dinner.")
print(guest_list[2] + " please come to my dinner.\n")

# 3-5. Changing Guest List: You just heard that one of your guests canít make the dinner, so you need to send out a
# new set of invitations. Youíll have to think of someone else to invite. Start with your program from Exercise 3-4.
# Add a print statement at the end of your program stating the name of the guest who canít make it. Modify your list,
# replacing the name of the guest who canít make it with the name of the new person you are inviting. Print a second
# set of invitation messages, one for each person who is still in your list.
missed_guest = guest_list.pop()
print(missed_guest + " could not make the party")
guest_list.append('Henry')
print('However, ' + guest_list[-1] + ' can make the party!\n')
print(guest_list[0] + " please come to my dinner.")
print(guest_list[1] + " please come to my dinner.")
print(guest_list[2] + " please come to my dinner.\n")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests
# to invite to dinner. Start with your program from Exercise 3-4 or Exercise 3-5. Add a print statement to the end of
# your program informing people that you found . bigger dinner table. Use insert() to add one new guest to the
# beginning of your list. Use insert() to add one new guest to the middle of your list.Use append() to add one new
# guest to the end of your list.Print a new set of invitation messages, one for each person in your list.
print("We have found a bigger dinner table!")
guest_list.insert(0, 'Bucky')
guest_list.insert(2, 'Chucky')
guest_list.append('Ducky')
print(guest_list[0] + " please come to my dinner.")
print(guest_list[1] + " please come to my dinner.")
print(guest_list[2] + " please come to my dinner.")
print(guest_list[3] + " please come to my dinner.")
print(guest_list[4] + " please come to my dinner.")
print(guest_list[5] + " please come to my dinner.\n")

# Shrinking Guest List: You just found out that your new dinner table wonít arrive in time for the dinner,
# and you have space for only two guests. Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner. Use pop() to remove guests from your list one at a
# time until only two names remain in your list. Each time you pop a name from your list, print a message to that
# person letting them know youíre sorry you canít invite them to dinner. Print a message to each of the two people
# still on your list, letting them know theyíre still invited. Use del to remove the last two names from your list,
# so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
print('Unfortunately, I can only invite 2 people to dinner.')
denied_guest = guest_list.pop()
print("Sorry, I can't invite you to my dinner anymore, " + denied_guest)
denied_guest = guest_list.pop()
print("Sorry, I can't invite you to my dinner anymore, " + denied_guest)
denied_guest = guest_list.pop()
print("Sorry, I can't invite you to my dinner anymore, " + denied_guest)
denied_guest = guest_list.pop()
print("Sorry, I can't invite you to my dinner anymore, " + denied_guest)
print("Glad we got rid of those losers am I right " + guest_list[0])
print("Glad we got rid of those losers am I right " + guest_list[1])
guest_list.remove('Gerald')
guest_list.remove('Bucky')
print(guest_list)  # Empty list

# Organize a list
# Sort method stores alphabetically
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
print('\n')
# Sort cars in reverse order
cars.sort(reverse=True)
print(cars)

# To maintain the original order of a list but present it in a sorted order, you can use the sorted() function.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list: ")
print(cars)
print("\nHere is the sorted list: ")
print(sorted(cars))
print("\n Here is the original list: ")
print(cars)
print('\n')
# When sorting, try and make sure that the list is in lowercase to make sure that everything sorts correctly

# Printing a list in reverse order
print("This is the reversed list: ")
cars.reverse()
print(cars)

# Finding the length of a list
print(len(cars))

# 8. Seeing the World: Think of at least five places in the world youíd like to visit. Store the locations in a list.
# Make sure the list is not in alphabetical order. Print your list in its original order. Donít worry about printing
# the list neatly, just print it as a raw Python list. Use sorted() to print your list in alphabetical order without
# modifying the actual list. Show that your list is still in its original order by printing it. Use sorted() to print
# your list in reverse alphabetical order without changing the order of the original list. Show that your list is
# still in its original order by printing it again. Use reverse() to change the order of your list. Print the list to
# show that its order has changed. Use reverse() to change the order of your list again. Print the list to show itís
# back to its original order. Use sort() to change your list so itís stored in alphabetical order. Print the list to
# show that its order has been changed. Use sort() to change your list so itís stored in reverse alphabetical order.
# Print the list to show that its order has changed.
locations = ['spain', 'japan', 'italy', 'indonesia', 'mexico']
print(locations)
print(sorted(locations))
print(locations)
sorted(locations, reverse=True)
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
print(locations.sort(reverse=True))
print("\n")

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 46), use len() to print a
# message indicating the number of people you are inviting to dinner.
length_of_guest_list = len(denied_guest)
print("There are " + str(length_of_guest_list) + " coming to the party.\n")

# 3-10. Every Function: Think of something you could store in a list. For example, you could make a list of
# mountains, rivers, countries, cities, languages, or anything else youíd like. Write a program that creates a list
# containing these items and then uses each function introduced in this chapter at least once.
languages = ['spanish', 'english', 'french', 'german', 'japanese']
print(languages[0])
print(languages[0].title())
print(languages[-1])
languages.append('chinese')
print(languages)
languages.insert(0, 'korean')
print(languages)
languages.pop()
print(languages)
del languages[0]
languages.remove('english')
languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)
print(sorted(languages))
languages.reverse()
print(languages)
print(len(languages))
print('\n')

# Index out of range means that you accessing something that is not in the list, check you indexing ([0]) is first of
# list remember. 3-11. Intentional Error: If you have not received an index error in one of your programs yet,
# try to make one happen. Change an index in one of your programs to produce an index error. Make sure you correct
# the error before closing the program. Will do in comment mode to not mess up entire code
# errored_list = []
# print(errored_list[-1]
# Cannot access because nothing is in the list.
