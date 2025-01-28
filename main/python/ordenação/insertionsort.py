import pygame
import random
import time

#config do pygame
pygame.init()
WIDTH, HEIGHT = 1024, 768
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Inserion Sort Visualizer")

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
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i] # o elemento a ser inserido na parte ordenada
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            draw_list(arr, color_positions=[j, j + 1])  # Destaca os elementos sendo movidos
            pygame.event.pump()  # Permite a atualização da janela de eventos sem esperar
            screen.fill(Indigo)
            draw_list(arr)
            pygame.display.update()
            j -= 1
        arr[j + 1] = key  # Insere o elemento na posição correta
        draw_list(arr, color_positions=[i])  # Destaca o elemento inserido
        pygame.event.pump()  # Permite a atualização da janela de eventos sem esperar
        screen.fill(Indigo)
        draw_list(arr)
        pygame.display.update()


#inicialização da lista random
arr = [random.randint(10, HEIGHT) for _ in range(100)]

#loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_list(arr)#desenha a lista do inicio
    insertion_sort(arr)#ordena a lista

    time.sleep(0.05)

pygame.quit()