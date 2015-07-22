import unittest
from calculator.Calculator import Calculator

class test_Operation(unittest.TestCase):

    def test_add_value_out_of_order_fails(self):
        with self.assertRaises(RuntimeError):
            calc = Calculator()
            calc.enter_value(5)
            calc.enter_value(5)
            calc.evaluate()

    def test_add_operation_out_of_order_fails(self):
        with self.assertRaises(RuntimeError):
            calc = Calculator()
            calc.enter_operation('add')
            calc.evaluate()

    def test_all_clear(self):
        calc = Calculator()
        calc.enter_value(5)
        calc.evaluate()
        self.assertEqual(calc.get_result(), 5)
        calc.all_clear()
        self.assertEqual(calc.get_result(), 0)

    def test_evaluate(self):
        calc = Calculator()
        calc.enter_value(5.0)
        calc.enter_operation('multiply')
        calc.enter_value(2.0)
        calc.enter_operation('divide')
        calc.enter_value(5.0)
        calc.enter_operation('add')
        calc.enter_value(18.0)
        calc.enter_operation('subtract')
        calc.enter_value(5.0)
        self.assertAlmostEqual(calc.evaluate(), 15.0, 13)
        self.assertAlmostEqual(calc.get_result(), 15.0, 13)

    def test_evaluate_failure_empty(self):
        with self.assertRaises(RuntimeError):
            calc = Calculator()
            calc.enter_operation('add')
            calc.evaluate()

    def test_evaluate_failure_missing_value(self):
        with self.assertRaises(RuntimeError):
            calc = Calculator()
            calc.enter_value(5)
            calc.enter_operation('add')
            calc.evaluate()
