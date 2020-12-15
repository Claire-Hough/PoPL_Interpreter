from rply import ParserGenerator
from my_ast import *
from errors import *
from my_lexer import *

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
    # ['NUMBER', 'VARIABLE', 'STRING', 'OPEN_PARENS', 'CLOSE_PARENS',
    #  'PLUS', 'MINUS', 'MUL', 'DIV', 'MOD', 'POWER', 'EQUALS',
    #  'LESS_THAN', 'GREATER_THAN', 'EQUAL_TO', 'LESS_OR_EQUAL',
    #  'GREATER_OR_EQUAL', 'AND', 'OR', 'NOT', 'IN', 'FOR', 'WHILE',
    #  'RANGE', 'IF', 'ELIF', 'ELSE', 'PRINT', 'STR', 'INT', 
    #  'NOT_EQUAL_TO', 'NEW_LINE', 'SUB_ASSIGNMENT', 'ADD_ASSIGNMENT', 'BOOLEAN'
    # ],
    ['NUMBER', 'VARIABLE', 'PLUS', 'MINUS', 'MUL', 'DIV', 'MOD', 'POWER', 'EQUALS',
    'STRING', 'OPEN_PARENS', 'CLOSE_PARENS','BOOLEAN', 'LESS_THAN', 'GREATER_THAN', 
    'EQUAL_TO', 'LESS_OR_EQUAL', 'NOT_EQUAL_TO',
    'LESS_THAN', 'GREATER_THAN', 'EQUAL_TO', 'LESS_OR_EQUAL', 'OR', 'AND', 'GREATER_OR_EQUAL'
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
        ('left', ['EQUALS']), 
        #('left', ['IF', 'ELSE', 'ELIF', 'WHILE', 'FOR', 'NEW_LINE',]),
        ('left', ['AND', 'OR',]),
        #('left', ['NOT',]),
        ('left', ['EQUAL_TO', 'NOT_EQUAL_TO', 'GREATER_OR_EQUAL','GREATER_THAN', 'LESS_THAN', 'LESS_OR_EQUAL',]),
        ('left', ['PLUS', 'MINUS', 'SUB_ASSIGNMENT', 'ADD_ASSIGNMENT,']),
        ('left', ['MUL', 'DIV', 'MOD', 'POWER',])
    ]
)

@pg.production('expression : VARIABLE EQUALS expression')
def statement_assignment(state, p):
   return Assignment(Variable(p[0].getstr()),p[2])

# def expression_var_assign(p):
#     left = p[0]
#     right = p[2]
#     return Variable(left, right)

@pg.production('expression : BOOLEAN')
def expression_boolean(state, p):
    # p is a list of the pieces matched by the right hand side of the rule
    return Boolean(True if p[0].getstr() == 'true' else False)

@pg.production('expression : NUMBER')
def expression_number(p):
    # p is a list of the pieces matched by the right hand side of the
    # rule
    return Number(int(p[0].getstr()))

@pg.production('expression : STRING')
def expression_string(state, p):
    return String(p[0].getstr().strip('"\''))

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

@pg.production('expression : expression NOT_EQUAL_TO expression')
@pg.production('expression : expression EQUAL_TO expression')
@pg.production('expression : expression GREATER_OR_EQUAL expression')
@pg.production('expression : expression LESS_OR_EQUAL expression')
@pg.production('expression : expression GREATER_THAN expression')
@pg.production('expression : expression LESS_THAN expression')
@pg.production('expression : expression AND expression')
@pg.production('expression : expression OR expression')
def expression_equality(state, p):
    left = p[0]
    right = p[2]
    check = p[1]
    
    if check.gettokentype() == 'EQUAL_TO':
        return Equal(left, right)
    elif check.gettokentype() == 'NOT_EQUAL_TO':
        return NotEqual(left, right)
    elif check.gettokentype() == 'GREATER_OR_EQUAL':
        return GreaterThanEqual(left, right)
    elif check.gettokentype() == 'LESS_OR_EQUAL':
        return LessThanEqual(left, right)
    elif check.gettokentype() == 'GREATER_THAN':
        return GreaterThan(left, right)
    elif check.gettokentype() == 'LESS_THAN':
        return LessThan(left, right)
    elif check.gettokentype() == 'AND':
        return And(left, right)
    elif check.gettokentype() == 'OR':
        return Or(left, right)
    else:
        raise LogicError("Shouldn't be possible")

@pg.error
def error_handler(state, token):
    # we print our state for debugging porpoises
    #print token
    pos = token.getsourcepos()
    if pos:
        raise UnexpectedTokenError(token.gettokentype())
    elif token.gettokentype() == '$end':
        raise UnexpectedEndError()
    else:
        raise UnexpectedTokenError(token.gettokentype())

parser = pg.build()

# state = ParserState()

# def parse(code, state=state):
#     result = parser.parse(lexer.lex(code),state)
#     return result