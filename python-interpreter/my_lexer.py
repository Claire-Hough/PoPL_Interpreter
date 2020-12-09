from rply import LexerGenerator

# try:
#     import rpython.rlib.rsre.rsre_re as re
# except:    
#     import re

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
lg.add('NEW_LINE', r'\n')

#Comparison
lg.add('LESS_THAN', r'<')
lg.add('GREATER_THAN', r'>')
lg.add('EQUAL_TO', r'==')
lg.add('NOT_EQUAL_TO' r'!=')
lg.add('LESS_OR_EQUAL', r'<=')
lg.add('GREATER_OR_EQUAL', r'>=')
lg.add('AND', r'and')
lg.add('OR', r'or')
lg.add('NOT', r'not')
lg.add('SUB_ASSIGNMENT', r'-=')
lg.add('ADD_ASSIGNMENT', r'+=')

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
lg.add('BOOLEAN', r'true(?!\w)|false(?!\w)')


#Ignoring
lg.ignore('\s+')
lg.ignore('#[^\n]*')

lexer = lg.build()

# def lex(source):

#     comments = r'(#.*)(?:\n|\Z)'
#     multiline = r'([\s]+)(?:\n)'
    
#     comment = re.search(comments,source)
#     while comment is not None:
#         start, end = comment.span(1)
#         assert start >= 0 and end >= 0
#         source = source[0:start] + source[end:] #remove string part that was a comment
#         comment = re.search(comments,source)

#     line = re.search(multiline,source)
#     while line is not None:
#         start, end = line.span(1)
#         assert start >= 0 and end >= 0
#         source = source[0:start] + source[end:] #remove string part that was an empty line
#         line = re.search(multiline,source)

#     print("source is now: %s" % source)

#     return lexer.lex(source)