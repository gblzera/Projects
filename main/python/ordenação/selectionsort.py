import pygame
import random
import time

# Configurações do Pygame
pygame.init()
WIDTH, HEIGHT = 1024, 768
FPS = 60  # Aumentando os frames por segundo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Selection Sort Visualizer")

# Definir as cores
DarkGray = (169,169,169)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Função para desenhar a lista
def draw_list(arr, color_positions=[]):
    screen.fill(DarkGray)
    bar_width = WIDTH / len(arr)
    for i, val in enumerate(arr):
        color = BLUE
        if i in color_positions:
            color = RED
        # Quando a lista estiver totalmente ordenada, todas as barras ficam verdes
        if arr == sorted(arr):
            color = GREEN
        pygame.draw.rect(screen, color, (i * bar_width, HEIGHT - val, bar_width, val))
    pygame.display.update()

# Função Selection Sort com animação
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Troca o menor elemento encontrado com o elemento na posição i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_list(arr, color_positions=[i, min_idx])  # Destaca as posições comparadas
        pygame.event.pump()  # Permite a atualização da janela de eventos sem esperar
        screen.fill(DarkGray)
        draw_list(arr)
        pygame.time.wait(50) #pausa para visualização
        pygame.display.update()

# Inicialização da lista aleatória
arr = [random.randint(10, HEIGHT) for _ in range(100)]

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_list(arr)  # Desenha a lista no início
    selection_sort(arr)  # Executa o Selection Sort

    time.sleep(0.5)  # Pausa antes de fechar

pygame.quit()
