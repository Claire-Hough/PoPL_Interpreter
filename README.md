# PoPL_Interpreter - Clairahs
- Claire Hough
- Sarah McLaughlin
- Sarah Sherman

# Description
This project is an interpreter for Python written in Python.\
Examples are printed to the console from "my_main.py".

Each input is divided into positional arguments by our parse generator that is then matched to existing token lexers accepted by the parser.
These tokens are organized in ascending order of precedence rules to disambiguate ambiguous production rules as they run their functions in that order.
Based on the pre-defined tokens, expressions are created where functions are then called and ran from my_ast.py.

This interpreter can parse:
- arithmetic operators (+, -, *, /, %, ^)
- conditional statements (<, <=, >, >=, ==, !=)
- comments (#)
- identifying strings and numbers
- support output operation (print function)

# How to Run
This program is run via the "my_main.py" file.\
No args are taken in; example inputs are hard-coded.\
\
pip install rply\
python3 my_main.py\
OR\
./my_main.py
