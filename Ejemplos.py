import pygame
import math

# Inicializar Pygame
pygame.init()

# Parámetros
n = 100  # Número total de cuadros
square_size = 50
padding = 10
squares = []

# Calcular el número de cuadros por fila
squares_per_row = math.ceil(math.sqrt(n))
width = squares_per_row * (square_size + padding)
height = math.ceil(n / squares_per_row) * (square_size + padding)

# Configurar la ventana
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Llenado Rápido de Cuadros")

# Crear la lista de posiciones de los cuadros
for row in range(math.ceil(n / squares_per_row)):
    for col in range(squares_per_row):
        if len(squares) < n:
            x = col * (square_size + padding)
            y = row * (square_size + padding)
            squares.append((x, y))

# Variables de control
current_square = 0
running = True

# Bucle principal
while running:
    screen.fill((255, 255, 255))  # Fondo blanco

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rellenar cuadros hasta alcanzar el índice actual
    for i in range(current_square):
        x, y = squares[i]
        pygame.draw.rect(screen, (255, 0, 0), (x, y, square_size, square_size))

    # Avanzar al siguiente cuadro sin pausa perceptible
    if current_square < len(squares):
        current_square += 1

    pygame.display.flip()  # Actualizar pantalla

# Salir de Pygame
pygame.quit()
