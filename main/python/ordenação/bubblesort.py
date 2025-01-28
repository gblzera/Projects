import pygame
import random
import time

#config do pygame
pygame.init()
WIDTH, HEIGHT = 1024, 768
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort Visualizer")

#Def as cores
Indigo = (75,0,130)
Thistle = (216,191,216)
DarkGray = (169,169,169)
BlueViolet = (138,43,226)

#function para desenhar a lista
def draw_list(arr, color_positions=[]):
    screen.fill(Indigo)
    bar_width = WIDTH / len(arr)
    for i, val in enumerate(arr):
        color = DarkGray
        if i in color_positions:
            color = Thistle
        #quando ordenado troca a cor
        if arr == sorted(arr):
            color = BlueViolet
        pygame.draw.rect(screen, color, (i * bar_width, HEIGHT - val, bar_width, val))
    pygame.display.update()

#function bubble sort com animação
def bubble_sort(arr):
    n = len(arr)
    for i in range (n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw_list(arr, color_positions=[j, j + 1])
                pygame.time.wait(10) #pausa para visualização
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

#inicialização da lista random
arr = [random.randint(10, HEIGHT) for _ in range(100)]

#loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_list(arr)#desenha a lista do inicio
    bubble_sort(arr)#ordena a lista

    time.sleep(0.05)

pygame.quit()