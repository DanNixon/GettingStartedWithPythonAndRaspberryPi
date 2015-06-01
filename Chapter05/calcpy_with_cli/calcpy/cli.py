from calcpy.calculator.Calculator import Calculator
import sys

def run_cli():
    calc = Calculator()

    for arg in sys.argv[1:]:
        try:
            value = float(arg)
            calc.enter_value(value)
        except ValueError:
            calc.enter_operation(arg)

    result = calc.evaluate()
    print result
