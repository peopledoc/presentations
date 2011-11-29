import unittest

class TestCase(unittest.TestCase):
	def test(self):
		list1 = range(15)
		list2 = range(2, 17)
		self.assertEqual(list1, list2)
		
if __name__ == '__main__':
	unittest.main()