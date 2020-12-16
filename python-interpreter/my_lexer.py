from rply import LexerGenerator

lg = LexerGenerator()

#Basic Lex stuffs
lg.add('NUMBER', r'\d+')
# lg.add('STRING', r'[a-zA-Z][a-zA-Z0-9_]*')
# lg.add('VARIABLE', r'STRING')
#lg.add('DIGIT', r'[0-9]')

#Operators
lg.add('POWER', r'\*\*')
lg.add('PLUS', r'\+')
lg.add('MINUS', r'-')
lg.add('MUL', r'\*')
lg.add('DIV', r'/')
lg.add('MOD', r'%')
# lg.add('EQUALS', r'=')

#Formatting
#lg.add('COLON', r':')
lg.add('OPEN_PARENS', r'\(')
lg.add('CLOSE_PARENS', r'\)')
#lg.add('NEW_LINE', r'\n')

#Comparison
lg.add('LESS_OR_EQUAL', r'<=')
lg.add('GREATER_OR_EQUAL', r'>=')
lg.add('LESS_THAN', r'<')
lg.add('GREATER_THAN', r'>')
lg.add('EQUAL_TO', r'==')
lg.add('NOT_EQUAL_TO', r'!=')
# lg.add('AND', r'and')
# lg.add('OR', r'or')
# lg.add('NOT', r'not')
# lg.add('SUB_ASSIGNMENT', r'-=')
# lg.add('ADD_ASSIGNMENT', r'\+=')

lg.ignore('\s+')

lexer = lg.build()