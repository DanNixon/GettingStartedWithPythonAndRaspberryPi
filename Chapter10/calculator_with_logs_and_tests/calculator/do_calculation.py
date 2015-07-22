#!/usr/bin/env python

import logging
from Calculator import Calculator

logging.basicConfig(level=logging.DEBUG)

c = Calculator()

c.enter_value(1)
c.enter_operation("add")
c.enter_value(9)
c.enter_operation("multiply")
c.enter_value(5)
c.enter_operation("divide")
c.enter_value(20)

print c.evaluate()

c.all_clear()
