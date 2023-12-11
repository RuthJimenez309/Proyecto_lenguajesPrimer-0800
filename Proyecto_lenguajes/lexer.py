import ply.lex as lex
import re


counter=0



# Definición de tokens
tokens = [
    'SL', 'VAL', 'COLUMNA', 'TILDE', 'TBL', 'WH', 'AMPERSAND', 'DEGREE', 'PERCENT',
    'LPAREN', 'RPAREN', 'ALLT', 'MINUS', 'IDENT', 'EQUALS', 'LESS_THAN',
    'GREATER_THAN', 'LESS_THAN_OR_EQUAL', 'GREATER_THAN_OR_EQUAL',
    'CHAR_LITERAL', 'INT_LITERAL', 'FLOAT_LITERAL'
]


# Expresiones regulares para tokens simples




t_AMPERSAND = r'&'
t_DEGREE = r'°'
t_PERCENT = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_THAN_OR_EQUAL = r'<='
t_GREATER_THAN_OR_EQUAL = r'>='
t_ignore = ' \t\r\n'


def increment():
   global counter
   counter+=1
   #print(contador)
   




def t_SL(t):
    r'sl'
    global counter
    if t.lexpos>0:
      print(f"Error: syntax error 'sl' should be at the beginning of the input. Found at index {t.lexpos}")
      t.lexer.skip(1)
    elif r'sl':
      counter= 1
      return t
    else:
      print(f"Error: 'sl' lex Error. Found at index {t.lexpos}")
         

def t_WH(t):
    r'wh'
    global counter
    #if contador == 6:
    #    print("Syntaxt error: no name column")
    increment()
    return t  

def t_VAL(t):
    r'![a-zA-Z_][a-zA-Z0-9_]*!'
    if counter == 4:
        print("Syntaxt error: no name column")
    increment()
    return t



def t_COLUMNA(t):
    r'\b([a-zA-Z_][a-zA-Z0-9_]+(?:-[a-zA-Z_][a-zA-Z0-9_]+)*)\b'
    global counter
    
    if counter == 0:
     print(f"Error: Lex error, missing SENTENCE sl. Found at index {t.lexpos}")
     t.lexer.skip(1)
    elif counter== 2:
     print(f"Error: Lex error, missing TILDE. Found at index {t.lexpos}")
     t.lexer.skip(1)
    elif counter== 3:
     print(f"Error: Lex error, missing WH. Found at index {t.lexpos}")
     t.lexer.skip(1)
    elif counter== 4:
     counter+=1
    elif counter== 5:
     print(f"Error: Lex error, missing VAL. Found at index {t.lexpos}")
     t.lexer.skip(1)
    elif counter== 7:
     print(f"Error: Lex error, missing INT. Found at index {t.lexpos}")
     t.lexer.skip(1)
    else:
        increment()
        return t


def t_TBL(t):
    r'~\s+([a-zA-Z_][a-zA-Z0-9_]*)'
    global counter
    if re.match(r'~\s*wh', t.value):  
            print("Syntax error: no column names specified")
            t.value = None
            return t
    if counter==1:
        print("Syntax error: no column names specified")
    if not re.match(r'~\s+([a-zA-Z_][a-zA-Z0-9_]*)', t.value):
        print("Lex error: the table must have a tilde() before the name")
        t.value = None
    print("LexToken(TILDE,'~',1," + str(t.lexpos) + ")")
    increment()
    return t


def t_MINUS(t):
    r'-'
    return t


def t_CHAR_LITERAL(t):
    r'\'[^\']*\''
    return t


def t_INT_LITERAL(t):
    r'\d+'
    t.value = int(t.value)
    if counter == 6:
        print("Syntaxt error: no name column")
    increment()
    return t


def t_FLOAT_LITERAL(t):
    r'\d+\.\d*|\.\d+'
    t.value = float(t.value)
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}' at index {t.lexpos} (ASCII code: {ord(t.value[0])})")
    t.lexer.skip(1)










# Expresiones regulares para tokens más complejos...
# Ignorar espacios en blanco y comentarios...


# Construcción del analizador léxico
lexer = lex.lex()












