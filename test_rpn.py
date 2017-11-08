import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_sub(self):
		result = rpn.calculate("5 3 -")
		self.assertEqual(2, result)
	def test_mult(self):
		result = rpn.calculate("8 4 *")
		self.assertEqual(32, result)
	def test_divide(self):
		result = rpn.calculate("18 3 /")
		self.assertEqual(6, result)
