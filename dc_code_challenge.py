# 1) Declare two variables, a string and an integer 
# named "fullName" and "age". Set them equal to your name and age.
# Python is dynamic, so you don't need to declare variables.
# They exist automatically in the first scope where they are assigned.
# All you need is to assign them
fullName = "Liz"
age = 29



# 2) Declare an empty array called "myArray". 
# Add the variables from #1 (fullName and age) to the empty array using the push method.
# Print to the console.
# There are no arrays, but there are lists.  There is no push, but there is an append.
# There is no console.log, there is simply the console.
myArray = []
myArray.append(fullName)
print myArray
myArray.append(age)
print myArray



# 3) Write a simple function that takes no parameters called "sayHello". 
# Make it print "Hello!" to the console when called.
# Call the function.
def sayHello():
	print "Hello!"
sayHello();



# 4) Declare a variable named splitName and set it equal to
# fullName split into two seperate objects in an array.
# (In other words, if the variable fullName is equal to "John Smith", then splitName should 
# equal ["John", "Smith"].)
# Print splitName to the console.
# HINT: Remember to research the methods and concepts listed in the instructions PDF.
fullName = "Liz Gulsby"
splitName = fullName.split(" ")
print splitName




# 5) Write another simple function that takes no parameters called "sayName".
# When called, this function should print "Hello, ____!" to the console, where the blank is 
# equal to the first value in the splitName array from #4.
# Call the function.  (In our example, "Hello, John!" would be printed to the console.)
def sayName():
	print "Hello, " + splitName[0]

sayName()





# 6) Write another function named myAge.  This function should take one parameter: the year you 
# were born, and it should print the implied age to the console.
# Call the function, passing the year you were born as the argument/parameter.
# HINT: http://www.w3schools.com/js/js_functions.asp
def myAge(year):
	print 2017 - year

myAge(1987)

 

# 7) Using the basic function given below, add code so that sum_odd_numbers will print to the console the sum of all the odd numbers from 1 to 5000.  Don't forget to call the function!
# HINT: Consider using a 'for loop'.
# Rewrite for Python
 

def sum_odd_numbers():
    total_sum = 0
    for i in range(1, 5000):
    	if i % 2 != 0:
    		total_sum += i
    print total_sum

sum_odd_numbers()
 