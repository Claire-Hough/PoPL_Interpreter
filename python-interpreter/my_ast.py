from rply.token import BaseBox
from errors import *


class Boolean(BaseBox):
    def __init__(self, value):
        self.value = bool(value)

    def eval(self, env):
        return self
    
    def rep(self):
        return 'Boolean(%s)' % self.value

class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        return self.value


class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Equal(BinaryOp):
    
    def rep(self):
        return 'Equal(%s, %s)' % (self.left.rep(), self.right.rep())
    
    def eval(self, env):
        return self.left.eval(env).equals(self.right.eval(env))

class NotEqual(BinaryOp):
    
    def rep(self):
        return 'NotEqual(%s, %s)' % (self.left.rep(), self.right.rep())
    
    def eval(self, env):
        result = self.left.eval(env).equals(self.right.eval(env))
        result.value = not result.value
        return result

class GreaterThanEqual(BinaryOp):
    
    def rep(self):
        return 'GreaterThan(%s, %s)' % (self.left.rep(), self.right.rep())
    
    def eval(self, env):
        return self.left.eval(env).gte(self.right.eval(env))

class LessThanEqual(BinaryOp):
    
    def rep(self):
        return 'LessThan(%s, %s)' % (self.left.rep(), self.right.rep())
    
    def eval(self, env):
        return self.left.eval(env).lte(self.right.eval(env))

class GreaterThan(BinaryOp):
    
    def rep(self):
        return 'GreaterThan(%s, %s)' % (self.left.rep(), self.right.rep())
    
    def eval(self, env):
        return self.left.eval(env).gt(self.right.eval(env))

class LessThan(BinaryOp):
    
    def rep(self):
        return 'LessThan(%s, %s)' % (self.left.rep(), self.right.rep())
    
    def eval(self, env):
        return self.left.eval(env).lt(self.right.eval(env))

class And(BinaryOp):
    
    def rep(self):
        return 'And(%s, %s)' % (self.left.rep(), self.right.rep())
    
    def eval(self, env):
        one = self.left.eval(env).equals(Boolean(True))
        two = self.right.eval(env).equals(Boolean(True))
        return Boolean(one.value and two.value)

class Or(BinaryOp):
    
    def rep(self):
        return 'Or(%s, %s)' % (self.left.rep(), self.right.rep())
    
    def eval(self, env):
        one = self.left.eval(env).equals(Boolean(True))
        two = self.right.eval(env).equals(Boolean(True))
        # must remember to use inner primitive values
        return Boolean(one.value or two.value)

class String(BaseBox):
    def __init__(self, value):
        self.value = str(value)

    def eval(self, env):
        return self

    def to_string(self):
        return '"%s"' % str(self.value)

    def rep(self):
        return 'String("%s")' % self.value

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
