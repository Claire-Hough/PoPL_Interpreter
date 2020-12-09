from rply import LexerGenerator

lg = LexerGenerator()

#Basic Lex stuffs
lg.add('NUMBER', r'\d+')
lg.add('STRING', r'[a-zA-Z][a-zA-Z0-9_]*')
lg.add('VARIABLE', r'STRING')
lg.add('DIGIT', r'[0-9]')
#lg.add('NUMBER', r'DIGIT+')

#Operators
lg.add('POWER', r'\*\*')
lg.add('PLUS', r'\+')
lg.add('MINUS', r'-')
lg.add('MUL', r'\*')
lg.add('DIV', r'/')
lg.add('MOD', r'%')
lg.add('EQUALS', r'=')

#Formatting
lg.add('COLON', r':')
lg.add('OPEN_PARENS', r'\(')
lg.add('CLOSE_PARENS', r'\)')

#Comparison
lg.add('LESS_THAN', r'<')
lg.add('GREATER_THAN', r'>')
lg.add('EQUAL_TO', r'==')
lg.add('LESS_OR_EQUAL', r'<=')
lg.add('GREATER_OR_EQUAL', r'>=')
lg.add('AND', r'and')
lg.add('OR', r'or')
lg.add('NOT', r'not')

#Loops, misc
lg.add('IN', r'in')
lg.add('FOR', r'for')
lg.add('WHILE', r'while')
lg.add('RANGE', r'range')

#If stuffs
lg.add('IF', r'if')
lg.add('ELIF', r'elif')
lg.add('ELSE', r'else')

#Misc functions
lg.add('PRINT', r'print')
lg.add('STR', r'str')
lg.add('INT', r'int')



#Ignoring
lg.ignore('\s+')
lg.ignore('#[^\n]*')

lexer = lg.build()