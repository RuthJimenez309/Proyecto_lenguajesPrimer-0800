from lexer import lexer
from parsers import parser

lexer.input("sl apellido ~ wh genero = !femenino! & edad > 18")


for tok in lexer:
    print(tok)
    
    
    
    #este es nuetrso programa

#lexer.input("sl apellido ~ norecuerdo wh genero = !femenino! & edad > 18")
