import pygame
import random
import time

#config do pygame
pygame.init()
WIDTH, HEIGHT = 1024, 768
FPS = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Merge Sort Visualizer")

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
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Encontra o meio da lista
        left_half = arr[:mid]  # Divide a lista pela metade
        right_half = arr[mid:]

        merge_sort(left_half)  # Ordena a metade esquerda
        merge_sort(right_half)  # Ordena a metade direita

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            draw_list(arr, color_positions=[i, j])  # Destaca as comparações
            pygame.event.pump()  # Permite a atualização da janela de eventos sem esperar
            screen.fill(Indigo)
            draw_list(arr)
            pygame.display.update()

        # Verifica se algum elemento da metade esquerda ficou
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            draw_list(arr, color_positions=[i])  # Destaca o elemento da metade esquerda
            pygame.event.pump()
            screen.fill(Indigo)
            draw_list(arr)
            pygame.display.update()

        # Verifica se algum elemento da metade direita ficou
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            draw_list(arr, color_positions=[j])  # Destaca o elemento da metade direita
            pygame.event.pump()
            screen.fill(Indigo)
            draw_list(arr)
            pygame.time.wait(250)
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
    merge_sort(arr)#ordena a lista

    time.sleep(200)

pygame.quit()