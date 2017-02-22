# dictionary is a fancy Python term for a JS object
# Must put keys (properties) in ""
# called key-value pairs in Python as opposed to (property, value) in others

# zombie = {
# 	'speed': 10,
# 	'power': 6,
# 	'hunger': 12,
# 	'name': 'Zombie'
# }

# print zombie['speed'] #bracket notation is what the rest of the world uses to print an attribute (key) of an object (instead of .speed) - can access any of the keys using bracket notation - Python will organize the key order how it wants unless you write a retention for the key order

# add a new key just like you do in JS
# vars are dynamic in Python
# not the same as a class-based system!  No functions/etc attached to it
# nice way to organize data

# zombie['weapon'] = 'Fist'
# zombie['startX'] = 200;
# zombie['startY'] = 200;
# print zombie

# Can change the value of an existing key, just like in JS
# if zombie['speed'] < 5:
# 	zombie['position'] = zombie['startX'] + 2;
# elif zombie['speed'] < 10:
# 	zombie['position'] = zombie['startX'] + 4;
# else:
# 	zombie['position'] = zombie['startX'] + 6;

# you can delete a key with del
# zombie['pointless'] = 'duh';
# del zombie['pointless'];
# print zombie

# Store all the techs we know in a dictionary and set the value from 1 - 10
# skill1 = 'Redux'
# techs = {
# 	"HTML": 1,
# 	"CSS": 2,
# 	"JS": 3,
# 	"jQuery": 4,
# 	"Node.js": 5,
# 	"React": 6,
# 	skill1: 7,
# 	"MySQL": 8,
# 	"T-SQL": 9,
# 	"Python": 10
# }

# print techs
# for loops through dictionaries start with the key (placeholder), value
# for key, value in techs.items():
# 	print value

# if zombie.has_key('mother_name'):
# 	print zombie['mother_name']

# for key in zombie:
# 	print zombie[key]

# just like in JS, you can put dictionaries inside of lists (objects in arrays)
# zombies = [];  #an empty list called zombies
# zombies.append({
# 	"speed": 10,
# 	"power": 6,
# 	"hunger": 5,
# 	"name": "Bill"
# });

# zombies.append({
# 	"speed": 5,
# 	"power": 16,
# 	"hunger": 9,
# 	"name": "Sven"
# });

# print zombies
# print zombies[0]  #returns Bill
# print zombies[0]['name'] #returns Bill's name only

# for zombie in zombies:
# 	print zombie['name']

# Just like JS objects, you can assign a list to a dictionary key
# zombies[0]['victims'] = [{}, 'Rishi', 'Anna'];
# print zombies[0]

# zombies[0]['victims'][0]['name'] = 'Sean'  #first item in the victims list, given the name Sean
# print zombies[0]

# Just like in JS, you can assign a dictionary to a dictionary
#new key called super mode added below
# zombie[0]['super mode'] = {
# 	# At night....
# 	'power': 23,
# 	'hunger': 20,
# 	'weapon': "baseball bat"
# }




#!!!!!!!!!!!!!!!!!!!!!!EXERCISES BELOW!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Exercise 1

# Given the following dictionary, representing a mapping from names to phone numbers:

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}
# Write code to do the following:

# Print Elizabeth's phone number.
print phonebook_dict['Elizabeth']

# Add a entry to the dictionary: Kareem's number is 938-489-1234.
phonebook_dict['Kareem'] = '938-489-1234'

# Delete Alice's phone entry.
del phonebook_dict['Alice']

# Change Bob's phone number to '968-345-2345'.
phonebook_dict['Bob'] = '968-345-2345'

# Print all the phone entries.
for key,value in phonebook_dict.items():
	print value

# In this exercise, are you using dynamic keys or fixed keys?
# dynamic?

#**********************************************************************
# Exercise 2: Nested Dictionaries

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
# Write a python expression that gets the email address of Ramit.
print ramit['email']

# Write a python expression that gets the first of Ramit's interests.
print ramit['interests'][0]

# Write a python expression that gets the email address of Jasmine.
print ramit['friends'][0]['email']

# Write a python expression that gets the second of Jan's two interests.
print ramit['friends'][1]['interests'][1]

# In this exercise, are you using dynamic keys or fixed keys?
# fixed?

#**********************************************************************
# Letter Summary

# Write a letter_histogram function that takes a word as its input, and returns a dictionary containing the tally of how many times each letter in the alphabet was used in the word. For example:
def letter_histogram(word):
	string = list(word)
	for letter in string:
		

letter_histogram('banana')



# In this exercise, are you using dynamic keys or fixed keys?

