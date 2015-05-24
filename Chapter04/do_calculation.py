from calculator.Calculator import Calculator

c = Calculator()

c.enter_value(1)
c.enter_operation("add")
c.enter_value(9)
c.enter_operation("multiply")
c.enter_value(5)
c.enter_operation("divide")
c.enter_value(20)

print c.evaluate()
