import pygame
import numpy as np
import time

# Configuración inicial
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 5
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE
FRAMERATE = 60
UPDATE_INTERVAL = 0.2  # Tiempo en segundos para actualizar la pantalla

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de la Vida")
clock = pygame.time.Clock()

# Inicialización de la cuadrícula
grid = np.zeros((GRID_WIDTH, GRID_HEIGHT), dtype=int)

# Función para dibujar la cuadrícula
def draw_grid():
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            color = (0, 255, 0) if grid[x, y] == 1 else (0, 0, 0)
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Función para actualizar la cuadrícula según las reglas del juego
def update_grid():
    global grid
    new_grid = np.copy(grid)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            total = np.sum(grid[max(0, x-1):min(x+2, GRID_WIDTH), max(0, y-1):min(y+2, GRID_HEIGHT)]) - grid[x, y]
            if grid[x, y] == 1 and (total < 2 or total > 3):
                new_grid[x, y] = 0
            elif grid[x, y] == 0 and total == 3:
                new_grid[x, y] = 1
    grid = new_grid

# Inicializar el grid con algunas células vivas
def initialize_grid():
    global grid
    grid = np.random.choice([0, 1], size=(GRID_WIDTH, GRID_HEIGHT), p=[0.8, 0.2])

initialize_grid()

running = True
last_update_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar la cuadrícula cada medio segundo
    current_time = time.time()
    if current_time - last_update_time > UPDATE_INTERVAL:
        update_grid()
        last_update_time = current_time

    # Dibujar la cuadrícula
    screen.fill((0, 0, 0))
    draw_grid()
    pygame.display.flip()

    clock.tick(FRAMERATE)

pygame.quit()
