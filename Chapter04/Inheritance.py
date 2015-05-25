#!/usr/bin/env python

class Function(object):

    def evaluate(self):
        raise NotImplementedError();


class BinaryOperation(object):

    _left_operand = None
    _right_operand = None

    def set_left_operand(self, value):
        self._left_operand = value

    def set_right_operand(self, value):
        self._right_operand = value


class Addition(Function, BinaryOperation):

    def evaluate(self):
       return self._left_operand + self._right_operand


class Subtraction(Function, BinaryOperation):

    def evaluate(self):
        return self._left_operand - self._right_operand


add = Addition()
add.set_left_operand(5)
add.set_right_operand(10)
print add.evaluate()

sub = Subtraction()
sub.set_left_operand(50)
sub.set_right_operand(23)
print sub.evaluate()
