import logging

class Operation(object):
    _operation = None

    def __init__(self, name):
        if name not in ["add", "subtract", "multiply", "divide"]:
            raise ValueError("%s is not a valid operation" % (name))
        self._operation = name

    def __str__(self):
        return self._operation

    def evaluate(self, a, b):
        logging.getLogger(__name__).info("Evaluating operation: %s" % (self._operation))
        logging.getLogger(__name__).debug("RHS: %f, LHS: %f" % (a, b))
        if self._operation == "add":
            return a + b
        elif self._operation == "subtract":
            return a - b
        elif self._operation == "multiply":
            return a * b
        elif self._operation == "divide":
            return a / b
