import ply.yacc as yacc
from lexer import tokens

# Definición de la gramática y reglas de producción


def p_cons(p):
    '''
    cons : SL cols TILDE tbl wh
    '''
    if p[1] == 'sl':
        print("Análisis sintáctico exitoso")
    else:
        raise SyntaxError("Error sintáctico: 'SL' debe estar al principio")

def p_cols(p):
    '''
    cols : col
         | col MINUS col
         | ALLT
         | subcons
    '''
    pass

def p_subcons(p):
    '''
    subcons : LPAREN SL cols TILDE tbl wh RPAREN
    '''
    pass

def p_col(p):
    '''
    col : IDENT
    '''
    
    pass

def p_tbl(p):
    '''
    tbl : IDENT
    '''
    pass

def p_wh(p):
    '''
    wh : WH cond
    '''
    pass

def p_cond(p):
    '''
    cond : wh cond
         | col op val
         | cond AMPERSAND cond
    '''
    pass

def p_op(p):
    '''
    op : EQUALS
       | LESS_THAN
       | GREATER_THAN
       | LESS_THAN_OR_EQUAL
       | GREATER_THAN_OR_EQUAL
    '''
    pass

def p_val(p):
    '''
    val : CHAR_LITERAL
        | INT_LITERAL
        | FLOAT_LITERAL
    '''
    pass

def t_error(t):
    t.lexer.skip(1)



# Manejo de errores sintácticos...

# Construcción del analizador sintáctico
parser = yacc.yacc()
