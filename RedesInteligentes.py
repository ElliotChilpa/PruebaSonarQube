import tkinter as tk
import math

def toggle_colors():
    for square in squares:
        current_color = canvas.itemcget(square, "fill")
        new_color = "white" if current_color == "red" else "red"
        canvas.itemconfig(square, fill=new_color)
    root.after(500, toggle_colors)  # Cambia los colores cada 500 milisegundos

def create_squares(n):
    square_size = 5
    padding = 5

    # Calcular el número de cuadros por fila y el tamaño del canvas
    squares_per_row = math.ceil(math.sqrt(n))
    canvas_width = squares_per_row * (square_size + padding)
    canvas_height = math.ceil(n / squares_per_row) * (square_size + padding)
    canvas.config(width=canvas_width, height=canvas_height)

    row, col = 0, 0
    for _ in range(n):
        x1 = col * (square_size + padding)
        y1 = row * (square_size + padding)
        x2 = x1 + square_size
        y2 = y1 + square_size
        square = canvas.create_rectangle(x1, y1, x2, y2, fill="red")
        squares.append(square)

        col += 1
        if col >= squares_per_row:
            col = 0
            row += 1

# Configurar la ventana principal
root = tk.Tk()
root.title("Parpadeo de Múltiples Cuadros")

# Crear un lienzo ajustable
canvas = tk.Canvas(root)
canvas.pack()

# Definir el número de cuadros
n = 1000  # Cambia este valor para ver más o menos cuadros

# Lista para almacenar los cuadros y crear n cuadros
squares = []
create_squares(n)

# Iniciar el parpadeo de todos los cuadros
root.after(500, toggle_colors)

# Ejecutar la aplicación
root.mainloop()
