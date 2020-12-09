from rply.token import BaseBox
from errors import *


class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        return self.value


class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Variable(BaseBox):
    def __init__(self, name):
        self.name = str(name)
        self.value = None

    def getname(self):
        return str(self.name)

    def eval(self, env):
        if env.variables.get(self.name, None) is not None:
            self.value = env.variables[self.name].eval(env)
            return self.value
        raise LogicError("Not yet defined")

    def to_string(self):
        return str(self.name)


class Assignment(BinaryOp):

    def rep(self):
        return 'Assignment(%s, %s)' % (self.left.rep(), self.right.rep())

    def eval(self, env):
        if isinstance(self.left, Variable):

            if env.variables.get(self.left.getname(), None) is None:
                env.variables[self.left.getname()] = self.right
                return self.right.eval(env)

            # otherwise raise error
            raise ImmutableError(self.left.getname())

        else:
            raise LogicError("Cannot assign to this")


class Add(BinaryOp):
    def eval(self, env):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self, env):
        return self.left.eval() - self.right.eval()


class Mul(BinaryOp):
    def eval(self, env):
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self, env):
        return self.left.eval() / self.right.eval()


class Mod(BinaryOp):
    def eval(self, env):
        return self.left.eval() % self.right.eval()


class Power(BinaryOp):
    def eval(self, env):
        return self.left.eval() ** self.right.eval()
