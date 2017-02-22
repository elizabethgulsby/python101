from rpg_hero import Hero;
# import hero....hero = hero.Hero();
from rpg_monsters import Goblin;

hero = Hero();
enemies = [Goblin()];

for enemy in enemies:
	# Loop through all the bad guys in the enemies list!
	print vars(enemy)
	# keep the loop going as long as both have health
	# while hero.health > 0 and enemy.health > 0:
	while hero.alive() and enemy.alive():
		# print off content
		print "What will you do?";
		print "1. Fight %s" % enemy.name;
		print "2. Run away!";
		print "> ",
		# get input from user
		input = int(raw_input());
		if input == 1:
			# user has chosen to fight!  Subtract health from enemy = hero power
			# enemy.health -= hero.power;
			hero.attack(enemy);
		elif input == 2:
			# user has chosen to run away. Break out of the while loop
			break;
		else:
			# user has malfunctioned.  Complain.
			print "Invalid choice %r" % input
		if enemy.alive():
			# user has made their choice.  Now it's the enemy's turn.
			# IF the enemy has health, subtract his power from the hero health
			# hero.health -= enemy.power;
			enemy.attack(hero);
	if hero.alive():
		# we know they won, because someone's health is < 0
		print "You won! The %s is defeated!" % enemy.name
	else:
		# we know the hero lost, because someone won and it was not he/her
		print "You were defeated by the ferocious %s!" % enemy.name