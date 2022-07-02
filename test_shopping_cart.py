import unittest

from product import Product

class TestShoppingCart(unittest.TestCase):

    def test_product_object(self):
        name = 'Car BMW'
        price = 30000.00

        product = Product(name, price)
        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price)
if __name__ == '__main__':
    unittest.main()
