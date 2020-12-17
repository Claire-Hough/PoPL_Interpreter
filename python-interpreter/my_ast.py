from rply.token import BaseBox

class Comment(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        pass

class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class String(BaseBox):
    def __init__(self, value):
        self.value = str(value)

    def eval(self):
        return self.value


class Variable(BaseBox):

    # self.variables = {}
    
    def __init__(self, name):
        self.name = str(name)
        self.value = value
        
    def getname(self):
        return str(self.name)

    def eval(self):
        self.variables = {}
        self.variables.append(str(self.name))
        # if variables.get(self.name, value) is not None:
        self.value = variables[self.name].eval()
        return self.value
       
    def to_string(self):
        return str(self.name)


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


class Assignment(BinaryOp):  
    # def eval(self, env):
    #     if isinstance(self.left,Variable):
        
    #         if env.variables.get(self.left.getname(), None) is None:
    #             env.variables[self.left.getname()] = self.right
    #             return self.right.eval(env)
    def eval(self):
        if isinstance(self.left):
            if Variable.variables.get(self.left.getname(), None) is None:
                Variable.variables[self.left.getname()] = self.right
                return self.right.eval()
            

class Equal(BinaryOp):
    
    def rep(self):
        return 'Equal(%s, %s)' % (self.left.rep(), self.right.rep())
    
    def eval(self):
        return self.left.eval() == self.right.eval()

class NotEqual(BinaryOp):
    
    def rep(self):
        return 'NotEqual(%s, %s)' % (self.left.rep(), self.right.rep())
    
    def eval(self):
        return self.left.eval() != self.right.eval()

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