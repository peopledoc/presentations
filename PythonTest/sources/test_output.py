class Sample(object):

	def test(self, a, b, c):
		print "Divider", b - c
		return a / (b - c)
		
import unittest

class TestCase(unittest.TestCase):

	def test_first(self):
		self.assertEqual(Sample().test(1, 4, 2), 1/2)
		
	def test_second(self):
		self.assertEqual(Sample().test(0, 2, 1), 0)
		
	def test_third(self):
		self.assertEqual(Sample().test(4, 3, 3), None)
		
if __name__ == '__main__':
	unittest.main()