from my_lexer import *
from my_parser import *


import unittest
import parser
import sys
from contextlib import contextmanager
from io import StringIO
from open_file import *
import open_file

class Environment(object):
    
    def __init__(self):
        self.variables = {}
        open_file.begin('test.py')


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

    def setUp(self):
        self.s = parser.ParserState()
        self.e = Environment()

    def test_addition(self):
        print(parser.parse(lexer.lex('1 + 3'),self.s).eval(self.e))

#parser.parse(lexer.lex(source), state=ParserState('test.py'))

# print(parser.parse(lexer.lex('1 + 3')).eval())

# print(parser.parse(lexer.lex('1 - 3')).eval())

# print(parser.parse(lexer.lex('1 * 3')).eval())

# print(parser.parse(lexer.lex('1 / 3')).eval())

# print(parser.parse(lexer.lex('1 % 3')).eval())

# print(parser.parse(lexer.lex('2 ** 3')).eval())

# print(parser.parse(lexer.lex('a = 2')).eval())

if __name__ == '__main__':
    unittest.main()