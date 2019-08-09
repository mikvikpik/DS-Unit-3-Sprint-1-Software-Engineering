""" Part 1 of SC"""

import random
class Product():
	""" A class for Acme Corporation products"""

	def __init__(self, name):
		""" Sets attributes for product"""
		self.name = name
		self.price = 10
		self.weight = 5
		self.flammability = 0.5
		self.identifier = random.randint(1000000 , 9999999)

		"""Part 2 of SC"""
	def stealability(self):
		"""Determines theft potential"""
		steal_factor = self.price / self.weight
		if steal_factor < 0.5:
			print("Not so stealable...")
		elif steal_factor > 1:
			print("Very stealable!")
		else:
			print("Kinda stealable.")

	def explode(self):
		"""Determines explosion risk"""
		boom_factor = self.flammability * self.weight
		if boom_factor < 10:
			print("...fizzle.")
		elif boom_factor > 50:
			print("...BABOOM!!")
		else:
			print("...boom!")


"""Part 3 of SC"""
class BoxingGlove(Product):
	"""A class specific to Boxing Gloves sold by Acme Corporation"""
	def __init__(self, name):
		"""Pulls attributes from Product class
		Then overwrites weight default"""
		super().__init__(name)
		self.weight = 10

	def explode(self):
		"""Boxing Glove cannot explode"""
		print("...it's a glove.")

	def punch(self):
		"Determines punch factor of glove"
		punchy = self.weight
		if punchy < 5:
			print("That tickles.")
		elif punchy > 15:
			print("OUCH!")
		else:
			print("Hey that hurt!")


