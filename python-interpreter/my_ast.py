from rply.token import BaseBox

class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()

class Mod(BinaryOp):
    def eval(self):
        return self.left.eval() % self.right.eval()

class Power(BinaryOp):
    def eval(self):
        return self.left.eval() ** self.right.eval()


class Equal(BinaryOp):
    
    def rep(self):
        return 'Equal(%s, %s)' % (self.left.rep(), self.right.rep())
    
    def eval(self):
        return self.left.eval().equals(self.right.eval())

class NotEqual(BinaryOp):
    
    def rep(self):
        return 'NotEqual(%s, %s)' % (self.left.rep(), self.right.rep())
    
    def eval(self):
        result = self.left.eval().equals(self.right.eval())
        result.value = not result.value
        return result

class GreaterThanEqual(BinaryOp):
    
    def rep(self):
        return 'GreaterThan(%s, %s)' % (self.left.rep(), self.right.rep())
    
    def eval(self):
        return (self.left.eval() >= self.right.eval())

class LessThanEqual(BinaryOp):
    
    def rep(self):
        return 'LessThan(%s, %s)' % (self.left.rep(), self.right.rep())
    
    def eval(self):
        return (self.left.eval() <= self.right.eval())

class GreaterThan(BinaryOp):
    
    def rep(self):
        return 'GreaterThan(%s, %s)' % (self.left.rep(), self.right.rep())
    
    def eval(self):
        return self.left.eval() > self.right.eval()

class LessThan(BinaryOp):
    
    def rep(self):
        return 'LessThan(%s, %s)' % (self.left.rep(), self.right.rep())
    
    def eval(self):
        return self.left.eval() < self.right.eval()