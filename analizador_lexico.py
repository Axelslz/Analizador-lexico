import ply.lex as lex



class analizadorlexico:
    
    tokens = [
        'IDENTIFICADORES', 'TIPO', 'SIGNOS',
        'CORCHETES', 'LLAVES', 'PALABRA_RESERVADA',
        'PARENTESIS', 'NUMERO', 'ASIGNACION', 'DESCONOCIDO', 'CADENA'
    ]

    t_ASIGNACION = r'\='
    t_CORCHETES = r'\[|\]'
    t_LLAVES = r'\{|\}'
    t_PARENTESIS = r'\(|\)'
    t_TIPO = r'\bint\b|\bstring\b'
    t_ignore = ' \t\n'

    def t_PALABRA_RESERVADA(self, t):
        r'contenido|Vi|War|Fun|Malph'
        return t

    def t_NUMERO(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_SIGNOS(self, t):
        r'[><;]'
        return t

    def t_IDENTIFICADORES(self, t):
        r'[a-zA-Z][a-zA-Z0-9]*'
        return t

    def t_CADENA(self, t):
        r'\"([^\\\n]|(\\.))*?\"'
        t.value = t.value[1:-1]  # Quitar las comillas dobles
        return t

    def __init__(self):
        self.lexer = lex.lex(module=self)
        self.error_list = []  # Lista para almacenar mensajes de error

    def t_error(self, t):
        valor = str(t.value)
        if valor.startswith('"') and not valor.endswith('"'):
            error_msg = f"Error: Cadena no cerrada en la posición {t.lexpos}"
            self.error_list.append(error_msg)
        else:
            error_msg = f"Carácter desconocido '{t.value[0]}' en la posición {t.lexpos}"
            self.error_list.append(error_msg)
        t.type = 'DESCONOCIDO'
        t.value = t.value[0]
        self.lexer.skip(1)
        return t

    def analyze(self, data):
        self.lexer.input(data)
        result = []
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            result.append((tok.type, tok.value))
        return result


