from rply import ParserGenerator
from my_ast import *
from errors import *

class ParserState(object):
    def __init__(self, filename):
        self.filename = filename

# state instance which gets passed to parser
# class ParserState(object):
#     def __init__(self):
#         # we want to hold a dict of declared variables
#         self.variables = {}
        
pg = ParserGenerator(
    # A list of all token names, accepted by the parser.
    ['NUMBER', 'VARIABLE', 'OPEN_PARENS', 'CLOSE_PARENS',
     'PLUS', 'MINUS', 'MUL', 'DIV', 'MOD', 'POWER', 'EQUALS',
     'LESS_THAN', 'GREATER_THAN', 'EQUAL_TO', 'LESS_OR_EQUAL', 
     'GREATER_OR_EQUAL', 'AND', 'OR', 'NOT', 'IN', 'FOR', 'WHILE',
     'RANGE', 'IF', 'ELIF', 'ELSE', 'PRINT', 'STR', 'INT'
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
        ('left', ['EQUALS']), 
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV'])
    ]
)

@pg.production('expression : VARIABLE EQUALS expression')
def statement_assignment(state, p):
   return Assignment(Variable(p[0].getstr()),p[2])

# def expression_var_assign(p):
#     left = p[0]
#     right = p[2]
#     return Variable(left, right)

@pg.production('expression : NUMBER')
def expression_number(p):
    # p is a list of the pieces matched by the right hand side of the
    # rule
    return Number(int(p[0].getstr()))

@pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
def expression_parens(p):
    return p[1]

@pg.production('expression : expression PLUS expression')
@pg.production('expression : expression MINUS expression')
@pg.production('expression : expression MUL expression')
@pg.production('expression : expression DIV expression')
@pg.production('expression : expression MOD expression')
@pg.production('expression : expression POWER expression')
def expression_binop(p):
    left = p[0]
    right = p[2]
    operator = p[1]
    if operator.gettokentype() == 'PLUS':
        return Add(left, right)
    elif operator.gettokentype() == 'MINUS':
        return Sub(left, right)
    elif operator.gettokentype() == 'MUL':
        return Mul(left, right)
    elif operator.gettokentype() == 'DIV':
        return Div(left, right)
    elif operator.gettokentype() == 'MOD':
        return Mod(left, right)
    elif operator.gettokentype() == 'POWER':
        return Power(left, right)
    else:
        raise AssertionError('Oops, this should not be possible!')

# @pg.production('expression : expression LESS_THAN expression')
# def 

parser = pg.build()