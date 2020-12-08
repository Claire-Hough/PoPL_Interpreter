import sys
from py_parser import *
from py_lexer import *

def usage():
    sys.stderr.write('Usage: py filename\n')
    sys.exit(1)

if __name__ == '__main__':
#    if len(sys.argv) != 2:
#        usage()
#    filename = sys.argv[1]
    filename = 'hello.py'
    text = open(filename).read()
    tokens = py_lex(text)

    for t in tokens:
        print(t)

    parse_result = py_parse(tokens)
    if not parse_result:
        sys.stderr.write('Parse error!\n')
        sys.exit(1)
    ast = parse_result.value
    env = {}
    ast.eval(env)

    sys.stdout.write('Final variable values:\n')
    for name in env:
        sys.stdout.write('%s: %s\n' % (name, env[name]))
