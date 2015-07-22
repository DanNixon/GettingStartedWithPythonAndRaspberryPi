import unittest
from calculator.Operation import Operation

class test_Operation(unittest.TestCase):

    def test_create_add(self):
        op = Operation('add')
        self.assertEqual(str(op), 'add')

    def test_create_subtract(self):
        op = Operation('subtract')
        self.assertEqual(str(op), 'subtract')

    def test_create_multiply(self):
        op = Operation('multiply')
        self.assertEqual(str(op), 'multiply')

    def test_create_divide(self):
        op = Operation('divide')
        self.assertEqual(str(op), 'divide')

    def test_create_fails(self):
        self.assertRaises(ValueError,
                          Operation,
                          'not_a_function')

    def test_add(self):
        op = Operation('add')
        result = op.evaluate(5, 2)
        self.assertEqual(result, 7)

    def test_subtract(self):
        op = Operation('subtract')
        result = op.evaluate(5, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        op = Operation('multiply')
        result = op.evaluate(5, 2)
        self.assertEqual(result, 10)

    def test_divide(self):
        op = Operation('divide')
        result = op.evaluate(5, 2)
        self.assertEqual(result, 2)
