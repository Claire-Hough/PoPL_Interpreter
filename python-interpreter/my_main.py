from my_lexer import *
from my_parser import *

parser.parse(lexer.lex(source), state=ParserState('test.py'))

# print(parser.parse(lexer.lex('1 + 3')).eval())

# print(parser.parse(lexer.lex('1 - 3')).eval())

# print(parser.parse(lexer.lex('1 * 3')).eval())

# print(parser.parse(lexer.lex('1 / 3')).eval())

# print(parser.parse(lexer.lex('1 % 3')).eval())

# print(parser.parse(lexer.lex('2 ** 3')).eval())

# print(parser.parse(lexer.lex('a = 2')).eval())