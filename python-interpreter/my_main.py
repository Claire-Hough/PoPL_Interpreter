from my_lexer import *
from my_parser import *

# Arithmetic operators
print("Addition: 1 + 3 =")
print(parser.parse(lexer.lex('1 + 3')).eval())
print("Subtraction: 1 - 3 =")
print(parser.parse(lexer.lex('1 - 3')).eval())
print("Multiplication: 1 * 3 =")
print(parser.parse(lexer.lex('1 * 3')).eval())
print("Division: 1 / 3 =")
print(parser.parse(lexer.lex('1 / 3')).eval())
print("Modulo: 15 % 10 =")
print(parser.parse(lexer.lex('15 % 10')).eval())
print("Power: 2 ** 3 =")
print(parser.parse(lexer.lex('2 ** 3')).eval())
print()

# Conditional Statements
print("Less Than: 1 < 3 =")
print(parser.parse(lexer.lex('1 < 3')).eval())
print("Less Than or Equal To: 1 <= 3 =")
print(parser.parse(lexer.lex('1 <= 3')).eval())
print("Greater Than: 1 > 3 =")
print(parser.parse(lexer.lex('1 > 3')).eval())
print("Greater Than or Equal To: 1 >= 3 =")
print(parser.parse(lexer.lex('1 >= 3')).eval())
print("Equal To: 1 == 3 =")
print(parser.parse(lexer.lex('1 == 3')).eval())
print("Not Equal To: 1 != 3 =")
print(parser.parse(lexer.lex('1 != 3')).eval())
print()

# Comments
print("Comment: '# This is a test'")
print(parser.parse(lexer.lex('# This is a test')).eval())
print("(Returns nothing because it is ignored)")
print()

# Print Statement
# print("Print Statement: print('This is a test')")
