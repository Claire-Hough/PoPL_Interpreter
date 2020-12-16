from my_lexer import *
from my_parser import *

# Arithmetic operators
print(parser.parse(lexer.lex('1 + 3')).eval())
print(parser.parse(lexer.lex('1 - 3')).eval())
print(parser.parse(lexer.lex('1 * 3')).eval())
print(parser.parse(lexer.lex('1 / 3')).eval())
print(parser.parse(lexer.lex('1 % 3')).eval())
print(parser.parse(lexer.lex('2 ** 3')).eval())

# Conditional Statements
print(parser.parse(lexer.lex('1 < 3')).eval())
#print(parser.parse(lexer.lex('1 <= 3')).eval())
print(parser.parse(lexer.lex('1 > 3')).eval())
#print(parser.parse(lexer.lex('1 >= 3')).eval())
#print(parser.parse(lexer.lex('1 == 3')).eval())
#print(parser.parse(lexer.lex('1 != 3')).eval())