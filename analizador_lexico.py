import ply.lex as lex
import tkinter as tk
from tkinter import scrolledtext

# resultado del análisis
resultado_lexema = []

reserved = {
    'int': 'INT',
    'func': 'FUNC',
    'repeat': 'REPEAT',
    'if': 'IF',
    'else': 'ELSE',
    'echo': 'ECHO',
    'return': 'RETURN',
}

tokens = list(reserved.values()) + [
    'IDENTIFICADOR',
    'ENTERO',
    'ASIGNAR',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',
    'MINUSMINUS',
    'PLUSPLUS',
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'DISTINTO',
    'PARIZQ',
    'PARDER',
    'LLAIZQ',
    'LLADER',
    'PUNTOCOMA',
    'COMA',
]

t_ASIGNAR = r'='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MINUSMINUS = r'\-\-'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'\^'

t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_IGUAL = r'=='
t_DISTINTO = r'!='
t_PUNTOCOMA = ';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_LLAIZQ = r'{'
t_LLADER = r'}'

t_ignore = ' \t'

def t_INT(t):
    r'int'
    return t

def t_FUNC(t):
    r'func\s+[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'FUNC')  # Busca en las palabras reservadas
    return t

def t_REPEAT(t):
    r'repeat'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ECHO(t):
    r'echo'
    return t

def t_RETURN(t):
    r'return|retornar'
    return t

def t_IDENTIFICADOR(t):
    r'\$\w+(_\d\w)*'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    global resultado_lexema
    estado = "** Token no válido en la Línea {:4} Valor {:16} Posición {:4}".format(
        str(t.lineno), str(t.value), str(t.lexpos)
    )
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Función para realizar el análisis léxico
def analizar_lexico(data):
    global resultado_lexema
    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Línea {:4} Tipo {:16} Valor {:16} Posición {:4}".format(
            str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos)
        )
        resultado_lexema.append(estado)
    return resultado_lexema

# Función que se llama al presionar el botón de análisis léxico
def analizar():
    entrada = entrada_text.get("1.0", tk.END)
    resultado = analizar_lexico(entrada)
    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, "\n".join(resultado))

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Analizador Léxico")

# Cuadro de texto de entrada
entrada_text = scrolledtext.ScrolledText(ventana, width=40, height=10, wrap=tk.WORD)
entrada_text.pack(padx=10, pady=10)

# Botón de análisis léxico
analizar_button = tk.Button(ventana, text="Analizar", command=analizar)
analizar_button.pack(pady=10)

# Cuadro de texto de resultado (más grande)
resultado_text = scrolledtext.ScrolledText(ventana, width=60, height=20, wrap=tk.WORD)
resultado_text.pack(padx=10, pady=10)

# Iniciar la interfaz gráfica
ventana.mainloop()
