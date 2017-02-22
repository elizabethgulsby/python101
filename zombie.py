class Zombie(object):
	def __init__(self, speed, strength, hunger, weapon, health): #this is like the constructor in JS - we're going to define this thing's setup - self is the first parameter - how it refers to itself going forward (Python's version of 'this')
		self.speed = speed;
		self.strength = strength;
		self.hunger = hunger;
		self.weapon = weapon;
		self.health = health;
		self.type = "zombie";

zombie_object = Zombie(6, 8, 19, 'bat', 15);
print zombie_object.speed;  #dot notation is reserved for objects - will print this zombie's speed
print dir(zombie_object);  # will return everything known about the zombie_object - would have to loop through list to cut out unwanted things here, which is everything flanked by double underscores
print vars(zombie_object); # will print all the keys + values about zombie_object (in format we're used to)
