""" Part 4 of SC"""
"""ACME CORPORATION OFFICIAL INVENTORY REPORT"""
from random import randint, sample, uniform
# from created file
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
product_list = []
product_weight = []
product_price = []
product_flame = []
product_full = []

def generate_products(self, products = 30):
	for product in range(products + 1):
		# product word complier
		word_1 = sample(ADJECTIVES, 1)[0]
		word_2 = sample(NOUNS, 1)[0]
		full_word = str(word_1) + " " + str(word_2)
		# stats compiler
		price = randint(5,100)
		weight = randint(5,100)
		flammability = uniform(0.0, 2.5)
		stats = (price, weight, flammability)
		product_stats = (fullword + str(stats))
		# append lists
		product_list.append(full_word)
		product_weight.append(weight)
		product_price.append(price)
		product_flame.append(flammability)
		product_full.append(product_stats) 

	return product_list


def inventory_report():
	print("\nACME CORPORATION OFFICIAL INVENTORY REPORT",
		"\nUnique Counts: ", sum(unique(product_list))
		"\nAverage Price: ", sum(product_price)/len(product_price),
		"\nAverage Weight: ", sum(product_weight)/len(product_weight),
		"\nAverage Flammability: ", sum(product_flame)/len(product_flame))


if __name__ == '__main__':
	inventory_report(generate_products())