import tkinter as tk
from tkinter import scrolledtext
import tkinter.messagebox as messagebox
from analizador_lexico import analizadorlexico  

# Función para limpiar el cuadro de texto de entrada
def limpiar_entrada():
    entrada_text.delete("1.0", tk.END)

# Función para realizar el análisis léxico y formatear los resultados
def analizar_lexico(data):
    lexer_analyzer = analizadorlexico()  
    result = lexer_analyzer.analyze(data)  

    resultados_formateados = []
    resultados_formateados.append(f'{"VALOR":<30}{"TOKEN":<20}')
    for tok_type, tok_value in result:
        resultado = f'{str(tok_value):<30}{str(tok_type):<20}'
        resultados_formateados.append(resultado)

    return resultados_formateados, lexer_analyzer.error_list

# Función que se llama al presionar el botón de análisis léxico
def analizar():
    entrada = entrada_text.get("1.0", tk.END)
    lexer_analyzer = analizadorlexico()  
    resultado, errores = analizar_lexico(entrada)
    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, "\n".join(resultado))
    
    # Mostrar alerta si hay tokens desconocidos
    if errores:
        messagebox.showerror("Errores encontrados", "\n".join(errores))

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
resultado_text = scrolledtext.ScrolledText(ventana, width=60, height=25, wrap=tk.WORD)
resultado_text.pack(padx=10, pady=10)

# Iniciar la interfaz gráfica
ventana.mainloop()
