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
    'CADENA',  # Token para cadenas de texto
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

t_ignore = ' \t\n'

def t_CADENA(t):
    r'\([^\)]*\)'
    t.value = t.value[1:-1]  
    return t

def t_INT(t):
    r'int'
    return t

def t_FUNC(t):
    r'func\s+[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'FUNC')  
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

# Función para limpiar el cuadro de texto de entrada
def limpiar_entrada():
    entrada_text.delete("1.0", tk.END)

# Función para realizar el análisis léxico y formatear los resultados
def analizar_lexico(data):
    global resultado_lexema
    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    resultados_formateados = []

    # Encabezado de la tabla
    resultados_formateados.append(f'{"VALOR":<30}{"LEXEMA":<20}')
    while True:
        tok = analizador.token()
        if not tok:
            break
        resultado = f'{str(tok.value):<30}{str(tok.type):<20}'
        resultados_formateados.append(resultado)
    
    return resultados_formateados 

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
entrada_text = scrolledtext.ScrolledText(ventana, width=90, height=0, wrap=tk.WORD)
entrada_text.pack(padx=10, pady=10)

# Marco para los botones
botones_frame = tk.Frame(ventana)
botones_frame.pack(pady=10)

# Botón de análisis léxico
analizar_button = tk.Button(botones_frame, text="Analizar", command=analizar)
analizar_button.pack(side=tk.LEFT, padx=5)

# Botón para limpiar la entrada
limpiar_button = tk.Button(botones_frame, text="Limpiar", command=limpiar_entrada)
limpiar_button.pack(side=tk.LEFT, padx=5)

# Cuadro de texto de resultado (más grande)
resultado_text = scrolledtext.ScrolledText(ventana, width=60, height=20, wrap=tk.WORD)
resultado_text.pack(padx=10, pady=10)

# Iniciar la interfaz gráfica
ventana.mainloop()

