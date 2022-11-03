from dataclasses import dataclass
import os


varibles = {}
file = open("test.pypp", "r")

@dataclass
class Tokens:
    
    SEMI = ";"
    EQUAlS = "="
    VAR = "var"
    NAME = ""
    INT = "int"
    FLOAT = "float"
    STRING = "string"
    CHAR = "char"
    CONST = "const"
    IF = "if"
    WHILE = "while"
    FOR = "for"
    SWITCH = "switch"
    CASE = "case"
    FUNCTION = "function"
    CLASS = "class"
    STRUCT = "struct"
    THIS = "this"
    IMPORT = "import"
    FROM = "from"


def add_variable(name, type, val):
    varibles[name] = [type, val]

def tokens():
    words = file.readlines().strip("\n").split()
    print(words)
    index = 0
    for line in words:
        if line == Tokens.VAR:
            name = words[index + 1]
            if words[index + 2] == Tokens.SEMI:
                add_variable(name, None, None)
                continue
            if words[index + 2] == Tokens.EQUAlS:
                value = words[index + 3]
                add_variable(name, Tokens.VAR, value)
            else: 
                raise Exception("Unexpected token after variable name")
        print(index)

        


tokens()
print(varibles)

# work on expeption class
# get each line read
