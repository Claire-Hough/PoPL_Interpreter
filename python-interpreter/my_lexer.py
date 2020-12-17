from rply import LexerGenerator

lg = LexerGenerator()

#Basic Lex stuffs
lg.add('PRINT', r'print')
lg.add('NUMBER', r'\d+')
lg.add('STRING', r'\'[a-zA-Z_][a-zA-Z0-9\s]*[$:?{!"[\]]*\'')
lg.add('IDENTIFIER', r'[a-zA-Z][a-zA-Z0-9_]*')
#lg.add('DIGIT', r'[0-9]')
lg.add('COMMENT', r'#[a-zA-Z0-9\s]*')
# lg.add('QUOTE', r'\'|\"')

#Operators
lg.add('POWER', r'\*\*')
lg.add('PLUS', r'\+')
lg.add('MINUS', r'-')
lg.add('MUL', r'\*')
lg.add('DIV', r'/')
lg.add('MOD', r'%')

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
lg.add('ASSIGNMENT', r'=')
# lg.add('AND', r'and')
# lg.add('OR', r'or')
# lg.add('NOT', r'not')
# lg.add('SUB_ASSIGNMENT', r'-=')
# lg.add('ADD_ASSIGNMENT', r'\+=')

lg.ignore('\s+')
# lg.ignore(r'#[a-zA-Z0-9\s]*')

lexer = lg.build()