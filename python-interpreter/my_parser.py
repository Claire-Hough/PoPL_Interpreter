from rply import ParserGenerator
from rply.token import BaseBox, Token
from my_ast import *
import os

pg = ParserGenerator(
    # A list of all token names, accepted by the parser.
    ['NUMBER', 'OPEN_PARENS', 'CLOSE_PARENS',
     'PLUS', 'MINUS', 'MUL', 'DIV', 'MOD', 'POWER',
     'LESS_THAN', 'GREATER_THAN', 'EQUAL_TO', 'LESS_OR_EQUAL',
     'GREATER_OR_EQUAL', 'NOT_EQUAL_TO', 'COMMENT', 'PRINT',
     'IDENTIFIER', 'ASSIGNMENT', 'STRING'
    #  'VARIABLE', 'STRING',  'EQUALS',
    #  'AND', 'OR', 'NOT', 'IN', 'FOR', 'WHILE',
    #  'RANGE', 'IF', 'ELIF', 'ELSE', 'PRINT', 'STR', 'INT', 
    #  'NEW_LINE', 'SUB_ASSIGNMENT', 'ADD_ASSIGNMENT', 'BOOLEAN'
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
        ('left', ['ASSIGNMENT']),
        ('left', ['EQUAL_TO', 'NOT_EQUAL_TO', 'GREATER_OR_EQUAL', 'LESS_OR_EQUAL', 'GREATER_THAN', 'LESS_THAN']),
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV', 'MOD', 'POWER'])
    ]
)


@pg.production('expression : COMMENT')
def expression_comment(p):
    return Comment(p[0].getstr())
    # can change this to not return at all if we want

@pg.production('expression : NUMBER')
def expression_number(p):
    # p is a list of the pieces matched by the right hand side of the
    # rule
    return Number(int(p[0].getstr()))

@pg.production('expression : STRING')
def expression_string(p):
    return String(p[0].getstr().strip('"\''))

@pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
def expression_parens(p):
    return p[1]

@pg.production('expression : PRINT OPEN_PARENS STRING CLOSE_PARENS')
@pg.production('expression : PRINT OPEN_PARENS NUMBER CLOSE_PARENS')
def expression_print(p):
    print(str(p[2].getstr()))

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
# @pg.production('expression : expression AND expression')
# @pg.production('expression : expression OR expression')
def expression_equality(p):
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
    # elif check.gettokentype() == 'AND':
    #     return And(left, right)
    # elif check.gettokentype() == 'OR':
    #     return Or(left, right)
    else:
        raise AssertionError('Oops, this should not be possible!')

@pg.production('expression : IDENTIFIER ASSIGNMENT expression')
def expression_binop(p):
    left = p[0]
    right = p[2]
    return Assignment(Variable(left.getstr()), right)

parser = pg.build()