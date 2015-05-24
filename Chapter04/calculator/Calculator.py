from Operation import Operation

class Calculator(object):
    _input_list = list()
    _result = 0.0

    def enter_value(self, value):
        if len(self._input_list) > 0 and not isinstance(self._input_list[-1], Operation):
            raise RuntimeError("Must enter an operation next")
        self._input_list.append(float(value))

    def enter_operation(self, operation_name):
        if len(self._input_list) == 0 or isinstance(self._input_list[-1], Operation):
            raise RuntimeError("Must enter a value next")
        self._input_list.append(Operation(operation_name))

    def evaluate(self):
        self._result = self._input_list[0]
        for idx in range(1, len(self._input_list), 2):
            operation = self._input_list[idx]
            next_value = self._input_list[idx + 1]
            self._result = operation.evaluate(self._result, next_value)
        
        return self._result

    def get_result(self):
        return self._result

    def all_clear(self):
        self._input_list = list()
        self._result = 0.0
