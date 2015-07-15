#!/usr/bin/env python

class Function(object):

    def evaluate(self):
        raise NotImplementedError();


class BinaryOperation(object):

    _left_operand = 0.0
    _right_operand = 0.0

    def set_left_operand(self, value):
        if not isinstance(value, float):
            raise ValueError("Value must be a float")
        self._left_operand = value

    def set_right_operand(self, value):
        if not isinstance(value, float):
            raise ValueError("Value must be a float")
        self._right_operand = value


class Addition(Function, BinaryOperation):

    def evaluate(self):
       return self._left_operand + self._right_operand


class Subtraction(Function, BinaryOperation):

    def evaluate(self):
        return self._left_operand - self._right_operand


add = Addition()
add.set_left_operand(5.0)
add.set_right_operand(10.0)
print add.evaluate()

sub = Subtraction()
sub.set_left_operand(50.0)
sub.set_right_operand(23.0)
print sub.evaluate()
