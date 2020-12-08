from my_lexer import *
from my_parser import *

print(parser.parse(lexer.lex('1 + 3')).eval())