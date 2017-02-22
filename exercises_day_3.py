# Given the following Person class:

class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1

    def print_contact_info(self):
    	print "%s's email: %s, %s's phone number: %s" % (self.name, self.email, self.name, self.phone)

    def add_friend(self, other_person):
    	print "%s" % other_person.name

    def num_friends(self):
    	print len(self.friends)




# Write code to

# Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

# Have sonny greet jordan using the greet method.
sonny.greet(jordan)

# Have jordan greet sonny using the greet method.
jordan.greet(sonny)

# Write a print statement to print the contact info (email and phone) of Sonny.
print sonny.email, sonny.phone

# Write another print statement to print the contact info of Jordan.
print jordan.email, jordan.phone

# ***************************************************************************

# Create a class Vehicle. A Vehicle object will have 3 attributes:

# make
# model
# year
# A vehicle is created thus:

# car = Vehicle('Nissan', 'Leaf', 2015)
# And you can access it's attributes individually like so:
# print car.make, car.model, car.year

# Add a print_info method to the Vehicle class. It will print out the vehicle's information like so:
class Vehicle(object):
	def __init__(self, make, model, year):
		self.make = make;
		self.model = model;
		self.year = year;
	def print_info(self):
		print "I'm a %s %s %s." % (self.year, self.make, self.model)

car = Vehicle('Lexus', 'IS250', '2017')
car.print_info()

# Go back to the Person class. Add a print_contact_info method to the Person class that will print out the contact info for a object instance of Person. You will use it thus:
# sonny.print_contact_info()
# Sonny's email: sonny@hotmail.com, Sonny's phone number: 483-485-4948
sonny.print_contact_info()

# Add a friends instance variable (attribute) to the Person class. You will initialize it to an empty list within the constructor (__init__). Once you've done this you should be able to add a friend to a person using list's append method:
jordan.friends.append(sonny)
sonny.friends.append(jordan)
print len(jordan.friends)
print len(sonny.friends)

# The fact that a person's friends attribute is a list is an implementation detail of the Person class. It is often desired to hide implementation details from the users of your object/class. Implement an add_friend method to Person, so that in order to add a friend, you'd only have to do:
jordan.add_friend(sonny)

# Similarly, to get the number of friends a person has, we'd like to hide the implementation detail that there is a friends attribute which is a list. Implement a num_friends method which returns the number of friends the person currently has:
jordan.num_friends()

# We want to count the number of times a person has greeted someone. To do this, we'll add another attribute, call it say greeting_count, and initialize it to 0. Then each time the greet method is called, we'll increment greeting_count by 1.
sonny.greeting_count
sonny.greet(jordan)
sonny.greeting_count






