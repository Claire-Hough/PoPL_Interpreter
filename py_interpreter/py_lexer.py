import lexer

RESERVED = 'RESERVED'
INT      = 'INT'
ID       = 'ID'
token_exprs = [
    (r'[ \n]+',                None),
    (r'[ \t]+',                None),
    # (r'#[^\n]*',               None),
    (r'#[A-Za-z][A-Za-z0-9_]*[\n]',             None),
    (r'#[A-Za-z][A-Za-z0-9_]*',             None),
    (r'#\s[A-Za-z][A-Za-z0-9_]*[\n]',             None),
    (r'#\s[A-Za-z][A-Za-z0-9_]*',             None),
    (r'#(\s[A-Za-z][A-Za-z0-9_])*',             None),
    (r'^\n',                   None),
    (r'=',                     RESERVED),
    (r'\(',                    RESERVED),
    (r'\)',                    RESERVED),
    (r':',                     RESERVED),
    (r';',                     RESERVED),
    (r'\+',                    RESERVED),
    (r'-',                     RESERVED),
    (r'\*',                    RESERVED),
    (r'/',                     RESERVED),
    (r'<=',                    RESERVED),
    (r'<',                     RESERVED),
    (r'>=',                    RESERVED),
    (r'>',                     RESERVED),
    (r'!=',                    RESERVED),
    (r'==',                    RESERVED),
    (r'and',                   RESERVED),
    (r'or',                    RESERVED),
    (r'not',                   RESERVED),
    (r'if',                    RESERVED),
    (r'then',                  RESERVED),
    (r'else',                  RESERVED),
    (r'elif',                  RESERVED),
    (r'while',                 RESERVED),
    (r'for',                   RESERVED),
    #(r'do',                    RESERVED),
    #(r'end',                   RESERVED),
    (r'[0-9]+',                INT),
    (r'[A-Za-z][A-Za-z0-9_]*', ID),
    (r'\n',                    None)
]

def py_lex(characters):
    return lexer.lex(characters, token_exprs)
