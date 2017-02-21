# print "Liz Gulsby"

# name = "Liz Gulsby"
# name = "Liz " + "Gulsby"
# fortyTwo = 40 + 2;
# print fortyTwo
# fortyTwo = 84 / 2;
# print fortyTwo;

# array...psyche! Lists (in Python)
animals = ['wolf', 'giraffe', 'hippo'];
print animals
print animals[0]
print animals[-1]  # gets the last element - hippo, here
animals.append('alligator');
print animals

# To delete an index, use the remove method
animals.remove('wolf')
print animals
# del animals[0] - also deletes an index where specified

# To go to a specific location: we can insert into any indice with "insert" (like splice)
animals.insert(0, 'zebra')
print animals
#To overwrite a certain index, see directly below
animals[0] = 'horse'
print animals

# pop works the same way - remove the last element
animals.pop()
print animals

#split works the same way as well (below, turning a string into an array)
dc_class = "Michael, Paul, Mason, Casey, Connie, Sarah, Andy"
dc_class_as_array = dc_class.split(", ")
print dc_class_as_array

#Sorted method will sort, but not change the actual array
print sorted(dc_class_as_array)
print dc_class_as_array # prints array as it was declared

sorted_class = sorted(dc_class_as_array)
print sorted_class

dc_class_as_array.sort(); #this will change the array from its original configuration
print dc_class_as_array

#Reverse method - reverses the array, NOT on value, but on index
dc_class_as_array.reverse()
print dc_class_as_array

# len attribute - works like .length in JS
print len(dc_class_as_array)
print dc_class_as_array[0] #will print Sarah because array was previously reversed

# slice in JS is [x:x]
# Creates a copy of the array; does not mutate the array
print dc_class_as_array[2:3]
print dc_class_as_array

# For loop is for>what_you_call_this_one>in>var
# no brackets!
for student in dc_class_as_array:
	# indentation matters in python!
	print student;

for i in range(1, 10):
	print i; #python will create the numbers for you

for i in range(0, len(dc_class_as_array)):
	print dc_class_as_array[i]

# functions in python - not a function! It is a "definition", ergo def:
def sayHello():
	# just like for loops, : is the curly brace in Python for functions
	# indentation matters, just like the for loop
	print "Hello, world!";

sayHello();

def say_hello_with_name(name, state = []):
	print "Hello, " + name;


name = "Liz"
say_hello_with_name(name);





















