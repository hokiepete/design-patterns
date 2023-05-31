# taken from https://tavianator.com/the-visitor-pattern-in-python/
import unittest
from abc import ABC


def _qualname(obj):
    """Get the fully-qualified name of an object (including module)."""
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj):
    """Get the name of the class that declared an object."""
    name = _qualname(obj)
    return name[:name.rfind('.')]


# Stores the actual visitor methods
_methods = {}


# Delegating visitor implementation
def _visitor_impl(self, arg):
    """Actual visitor method implementation."""
    key = (_qualname(type(self)), type(arg))
    if not key in _methods:
        raise Exception('Key % not found' % key)
    method = _methods[key]
    return method(self, arg)


# The actual @visitor decorator
def visitor(arg_type):
    """Decorator that creates a visitor method."""

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator

# ↑↑↑ LIBRARY CODE ↑↑↑

class Value:
    def __init__(self, value):
        self.value = value


class AdditionExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left


class MultiplicationExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left


class ExpressionPrinter:
    def __init__(self):
        # todo :)
        self.expression = []

    def __str__(self):
        # todo
        return ''.join(self.expression)

    @visitor(AdditionExpression)
    def visit(self, ae):
        self.expression.append("(")
        self.visit(ae.left)
        self.expression.append("+")
        self.visit(ae.right)
        self.expression.append(")")

    @visitor(MultiplicationExpression)
    def visit(self, me):
        # self.expression.append("(")
        self.visit(me.left)
        self.expression.append("*")
        self.visit(me.right)
        # self.expression.append(")")

    @visitor(Value)
    def visit(self, va):
        self.expression.append(str(va.value))


simple = AdditionExpression(Value(2), Value(3))
ep = ExpressionPrinter()
ep.visit(simple)
print("(2+3)", str(ep))

expr = MultiplicationExpression(
    AdditionExpression(Value(2), Value(3)),
    Value(4)
)
ep = ExpressionPrinter()
ep.visit(expr)
print("(2+3)*4", str(ep))