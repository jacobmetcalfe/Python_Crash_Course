# Chapter 2, Variable Types
message = "Hello World"
print(message)

message_to_title = "jacob metcalfe"
print(message_to_title.title())  # capitalizes the first letter of each word

print(message_to_title.upper())  # Message to capitalize all of

print(message_to_title.lower())  # Message to put in all lowercase

first = "Jacob"  # Stores first and last name in full and prints welcome message using title capitalization
second = "Metcalfe"
full = first + " " + second
print(full)
print("Hello " + full.title() + "!")

# White Space Name
# new line
print("Jacob \nMetcalfe")
# Tab up
print("Jacob \tMetcalfe")

# Removing Whitespace
whitespace_message = "    Whitespace sucks  "
# Removing Right Whitespace
whitespace_message = whitespace_message.rstrip()
print(whitespace_message)
# Removing Left Whitespace
whitespace_message = whitespace_message.lstrip()
print(whitespace_message)
# Removing All Whitespace
whitespace_message = whitespace_message.strip()
print(whitespace_message)

# 2-3 Personal Message: Store a personís name in a variable, and print a message to that person. Your message should
# be simple, such as, ìHello Eric, would you like to learn some Python today?î
name = "jacob"
print("Hello " + name.title() + ", Would you like to learn some Python today?")

# 2-4. Name Cases: Store a personís name in a variable, and then print that personís name in lowercase, uppercase,
# and titlecase.
print(name.lower())
print(name.upper())
print(name.title())

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author.
print("Ricky Bobby once said 'If you're not first, you're last'")

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous personís name in a variable called
# famous_person. Then compose your message and store it in a new variable called message. Print your message.
ricky_Bobby = "Ricky Bobby"
print(ricky_Bobby + " once said 'If you're not first, you're last'")

# 2-7. Stripping Names: Store a personís name, and include some whitespace characters at the beginning and end of the
# name. Make sure you use each character combination, "\t" and "\n", at least once.
ricky_Bobby_white = "   Ricky Bobby  "
print(ricky_Bobby_white.rstrip())
print(ricky_Bobby_white.lstrip())
print(ricky_Bobby_white.strip())

# Simple Math operations
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)

# Exponents
print(2 ** 3)

# int = whole number
# Float= decimal to one number
# Double = decimal with many numbers

# Birthday Message, simple cast from int to string
age = 23
bday_msg = "Happy " + str(age) + "rd Birthday!"
print(bday_msg)

# how int's will automatically round and print to the nearest whole number, can be switched if you do it as a double
# or float etc. if you want more precise numbers

# 2-8. Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the
# number 8. Be sure to enclose your operations in print statements to see the results.
print(5 + 3)
print(int(16 / 2))
print(11 - 3)
print(4 * 2)
print(2 ** 3)

# 2-9. Favorite Number: Store your favorite number in a variable. Then, using that variable, create a message that
# reveals your favorite number. Print that message.
fav_num = 14
print("My favorite number is " + str(fav_num))

# comments section 2-10. Adding Comments: Choose two of the programs youíve written, and add at least one comment to
# each. If you donít have anything specific to write because your programs are too simple at this point,
# just add your name and the current date at the top of each program file. Then write one sentence describing what
# the program does. This is a comment

# Note, write code that works, then review it and clean it up to make it more efficient and look better all equalling
# simplicity

# 2-11. Zen of Python: Enter import this into a Python terminal session and skim through the additional principles.
import this

print("\n\n")
