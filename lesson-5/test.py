import unittest
import fibo
import example_1
import example_7
# import importlib  
# foobar = importlib.import_module("example-7.py")

fibo.fib(1000)
example_7.hello()

class TestExample_1(unittest.TestCase):
	def testAGreaterThanB(self):
		self.assertTrue(example_1.aGreaterThanB(1, 2))
		self.assertFalse(example_1.aGreaterThanB(3, 2))

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()