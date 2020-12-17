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

# String
print("String:")
print(parser.parse(lexer.lex("'Here is a string'")).eval())
print()

# Assignment Operators
# print("Assignment: x = 2; x =")
# print(parser.parse(lexer.lex('x = 2')).eval())
# print()

# Print Statement
print("Print String: print('This is 1 test')")
parser.parse(lexer.lex("print('This is 1 test')"))
print("Print Number: print(12)")
parser.parse(lexer.lex("print(12)"))