from dataclasses import dataclass
import os
import time
from typing import List


# { name : [type, value] }
# { name : {type : int, value : 3, scope : global, "const" : False} }

variables = {}
functions = {}
classes = {}

@dataclass
class Tokens:
    
    SEMI = ";"
    EQUALS = "="
    VAR = "var"
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
    DEFAULT = "default"
    FUNCTION = "function"
    CLASS = "class"
    STRUCT = "struct"
    THIS = "this"
    IMPORT = "import"
    FROM = "from"

def find_variable(line: List):

    name = line[1]
    value = line[3] if line[2] == "=" else None 
    if value in variables:
        value = variables[value][1]
    if name in variables:
        raise Exception("Can not define variable that has arleady been defined")
    if line[2] == Tokens.SEMI:
        add_variable(name, Tokens.VAR, None)
    elif line[2] == Tokens.EQUALS:
        pass
    else: 
        raise Exception("Unexpected token after variable name")
    
    # finding data types
    if line[0] == Tokens.VAR:
        add_variable(name, Tokens.VAR, value)
    elif line[0] == Tokens.INT:
        try:
            value = int(value)
            add_variable(name, Tokens.INT, value)
        except ValueError:
            raise ValueError("Data type does not match value provided")
    elif line[0] == Tokens.FLOAT:
        try:
            value = float(value)
            add_variable(name, Tokens.FLOAT, value)
        except ValueError:
            raise ValueError("Data type does not match value provided")
    elif line[0] == Tokens.CHAR:
        add_variable(name, Tokens.CHAR, value)
    elif line[0] == Tokens.STRING:
        add_variable(name, Tokens.STRING, value)

    #non declare things

    if line[0] in variables:
        if name == Tokens.EQUALS:
            add_variable(line[0], variables[line[0]][0], line[2])
        else:
            raise Exception("There must be a equals sign to set value ")
    elif line[0] not in variables and line[1] is Tokens.EQUALS:

        raise Exception("must define variables with var or data type keywords")


def add_variable(name, type, val):
    variables[name] = [type, val]

def tokens(file):
    file = open(file, "r")
    lines = file.readlines()
    index = 0
    for line in lines:  
        
        line = line.strip("\n").split(" ")
        if line == [""]:
            continue
        find_variable(line)                                              
        
        index += 1


    print(variables)

tokens("test.pypp")