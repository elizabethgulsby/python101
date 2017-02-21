# An list/array is great, but it's changeable!  What if you wanted something that wasn't changeable to keep programmers from breaking your code? Or, you just wanted to be functional?

# Tuple - constant array

# a_tuple = (1,3,8)
# print a_tuple
# print a_tuple[2]
# a_tuple[2] = 5  won't work - can't mess with item assignment

# loop through tuples the same way you loop through lists
# for number in a_tuple:
# 	print number

# teams = ('Falcons', 'Hawks', 'atl_united', 'Silverbacks')

# for team in teams:
# 	if team == 'Hawks':
# 		print "Go Hawks!"
# 	else:
# 		print "It's basketball season!"


# team_a = 'Falcons'
# print team_a == 'Falcons'  #prints true or false instead of 1 or 0


# >, <, >=, <= are the same in Python
# OR and AND work the same way, just without the parens
# team_b = 'Braves'
# cond1 = (team_a == 'Falcons')
# cond2 =  (team_b == 'Braves')
# if cond1 and cond2:
# 	print 'Hooray!'

# Python's version of indexof is simply "in"
# print 'Hawks' in teams

# for team in teams:
# 	if team == 'Hawks':
# 		print 'Go Hawks!'
# 	elif team == 'Falcons':
# 		print 'Sad Super Bowl'

# if 'Hawks' in teams:
# 	print 'Go Hawks!'
# elif 'Falcons' in teams:
# 	print 'Go Falcons!'


# message = raw_input("Please enter your name");

# height = raw_input("In inches, how tall are you?\n");
# if (int(height) >= 42):
# 	print "You are tall enough to go on the Batman rollercoaster!";
# else:
# 	print "Maybe try the kiddie coaster.";


# while loop
from random import *
answer = randint(1, 1000)
# print answer
# current = 1
# while (current < 10):
# 	print current;
# 	current += 1;

# while answer != 1001:
prompt = raw_input("Say start to start the game!\n")
new_prompt = "start"

while (new_prompt != 'start'):
	print "You gotta say 'start'!"

