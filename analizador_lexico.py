import ply.lex as lex
import tkinter as tk
from tkinter import scrolledtext
import tkinter.messagebox as messagebox

class analizadorlexico:

    tokens = [
        'IDENTIFICADORES', 'TIPO', 'SIGNOS',
        'CORCHETES', 'LLAVES', 'PALABRA_RESERVADA',
        'PARENTESIS', 'NUMERO', 'ASIGNACION', 'DESCONOCIDO',
        'VARIABLE', 'FUNCION', 'RETORNAR', 'REPEAT', 'IF', 'ELSE', 'ECHO',
        'CADENA'
    ]

    t_ASIGNACION = r'\='
    t_CORCHETES = r'\[|\]'
    t_LLAVES = r'\{|\}'
    t_PARENTESIS = r'\(|\)'
    t_TIPO = r'\bint\b|\bstring\b'
    t_ignore = ' \t'

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Actualización de palabras reservadas
    def t_PALABRA_RESERVADA(self, t):
        r'\bint\b|\bfunc\b|\bretornar\b|\brepeat\b|\bif\b|\belse\b|\becho\b'
        return t

    def t_NUMERO(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_SIGNOS(self, t):
        r'[><;,+]'
        return t

    def t_IDENTIFICADORES(self, t):
        r'[a-zA-Z][a-zA-Z0-9]'
        return t

    def t_VARIABLE(self, t):
        r'\$[a-zA-Z][a-zA-Z0-9]*'
        return t

    # Actualización para reconocer 'func' como FUNCION
    def t_FUNCION(self, t):
        r'\bfunc\b'
        return t

    # Actualización para reconocer 'retornar' como RETORNAR
    def t_RETORNAR(self, t):
        r'\bretornar\b'
        return t

    # Actualización para reconocer 'repeat' como REPEAT
    def t_REPEAT(self, t):
        r'\brepeat\b'
        return t

    # Actualización para reconocer 'if' como IF
    def t_IF(self, t):
        r'\bif\b'
        return t

    # Actualización para reconocer 'else' como ELSE
    def t_ELSE(self, t):
        r'\belse\b'
        return t

    # Actualización para reconocer 'echo' como ECHO
    def t_ECHO(self, t):
        r'\becho\b'
        return t

    def t_CADENA(self, t):
        r'\"([^\\\"]|\\.)*\"'
        return t


    def t_error(self, t):
        error_message = f"Error de caracter '{t.value[0]}' en la línea {t.lineno}"
        print(error_message)
        self.error_list.append(error_message)
        t.lexer.skip(1)

    def __init__(self):
        self.lexer = lex.lex(module=self)
        self.error_list = []

    def analyze(self, data):
        self.lexer.input(data)
        result = []
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            result.append((tok.type, tok.value))
        return result

lexer_analyzer = analizadorlexico()
input_data = """
int $numero = 10;
func suma(int $a, int $b){retornar $a + $b;}
repeat (int $i = 0; $i < 10; $i++) {echo($i);}
if ($numero > 5) {echo("El número es mayor a 5");} else {echo("El número es menor a 5");}
func main() {echo("Inicio del programa");}
"""
result = lexer_analyzer.analyze(input_data)
