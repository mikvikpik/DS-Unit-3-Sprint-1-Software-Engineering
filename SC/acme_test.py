import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

     def test_stealability(self):
     	"""Test to check accurate stealability"""
     	steal_test = Product('Test Product')
     	self.assertEqual(prod.stealability, "Very stealable!")

     def test_explode(self):
     	"""Test to check exploding chance"""
     	explode_test = Product('Test Product')
     	self.assertEqual(prod.explode, "...fizzle.")


class AcmeReportTests(unittest.TestCase):
	"""Checking on Acme report"""
	def test_default_num_products(self):
		"""Testing for number of products in generated report"""
		report = generate_products()
		self.assertEqual(len(report), 30)

	def test_legal_names(self):
		"""Testing for possible generated names"""
		names = generate_products()
		self.assertIn(ADJECTIVES, generate_products)
		self.assertIn(NOUNS, generate_products)

if __name__ == '__main__':
    unittest.main()

