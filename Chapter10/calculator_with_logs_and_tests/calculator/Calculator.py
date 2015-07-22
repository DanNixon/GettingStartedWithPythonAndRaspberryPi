import logging
from Operation import Operation

class Calculator(object):
    _input_list = []
    _result = 0.0

    def __init__(self):
        self._input_list = []
        self._result = 0.0

    def enter_value(self, value):
        if len(self._input_list) > 0 and not isinstance(self._input_list[-1], Operation):
            raise RuntimeError("Must enter an operation next")

        logging.getLogger(__name__).info("Adding value: %f" % (value))
        self._input_list.append(float(value))

    def enter_operation(self, operation_name):
        if len(self._input_list) == 0 or isinstance(self._input_list[-1], Operation):
            raise RuntimeError("Must enter a value next")

        logging.getLogger(__name__).info("Adding operation: %s" % (operation_name))
        self._input_list.append(Operation(operation_name))

    def evaluate(self):
        logging.getLogger(__name__).info("Evaluating calculation")

        self._result = self._input_list[0]
        for idx in range(1, len(self._input_list), 2):
            operation = self._input_list[idx]
            next_value = self._input_list[idx + 1]

            logging.getLogger(__name__).debug("Next function: %f %s %f" % (
                self._result, str(operation), next_value))
            self._result = operation.evaluate(self._result, next_value)

        logging.getLogger(__name__).info("Result is: %f" % (self._result))
        return self._result

    def get_result(self):
        return self._result

    def all_clear(self):
        logging.getLogger(__name__).info("Clearing calculator")
        self._input_list = []
        self._result = 0.0
