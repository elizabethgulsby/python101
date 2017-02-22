from zombie import Zombie
import hero 

# make a zombie object from the class
zombie_object = Zombie(6,8,19, 'bat', 15);

# ugly version of print, but it gets you everything
# print dir(zombie_object);

#what you're used to
# print vars(zombie_object);

# Make a hero object from the hero class 
heroObject = hero.Hero();
# print vars(hero);
# hero.cheer_hero(heroObject);
heroObject.cheer_hero();
