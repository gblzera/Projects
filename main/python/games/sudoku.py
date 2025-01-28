import pygame
import random

pygame.init()

# cores
BRANCO = (255,255,255)
PRETO = (0,0,0)
CINZA = (200,200,200)

#tamanhos
LARGURA_TELA = 540
ALTURA_TELA = 540
CELULA_SIZE = 60
MARGEM = 5
LINHAS = 9
COLUNAS = 9

#cirar a tela
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Sudoku") 

#desenhar o tabuleiro
def desenhar_tab(tabuleiro):
    tela.fill(BRANCO)

    #desenhando as linhas principais:
    for i in range(LINHAS + 1):
        espaco = i * CELULA_SIZE
        if i % 3 == 0:
            pygame.draw.line(tela, PRETO, (espaco, 0), (espaco, ALTURA_TELA), 4) #grossa
            pygame.draw.line(tela, PRETO, (0, espaco), (LARGURA_TELA, espaco), 4) #grossa
        else:
            pygame.draw.line(tela, CINZA, (espaco, 0), (espaco, ALTURA_TELA), 1) #fina
            pygame.draw.line(tela, CINZA, (0, espaco), (LARGURA_TELA, espaco), 1) #fina
    
    #desenhando os num
    fonte = pygame.font.Font(None, 36)
    for i in range(LINHAS):
        for j in range(COLUNAS):
            numero = tabuleiro[i][j]
            if numero != 0:
                texto = fonte.render(str(numero), True, PRETO)
                tela.blit(texto, (j * CELULA_SIZE + 28, i * CELULA_SIZE + 20)) #posição do nuemro na celular
    
    pygame.display.flip()

#função para gerar um tabuleiro simples
def gerar_tabuleiro():
    tabuleiro = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],  #gerado manualmente ou por um algoritmo (pode pedir pro ChatGEPETO gerar um tabuleiro e subsutituir aqui)
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    return tabuleiro

# função principal do jg
def jogo():
    tabuleiro = gerar_tabuleiro()
    rodando = True
    selecionando = None

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                print("Clique detectado")
                x, y = pygame.mouse.get_pos()
                coluna = x // CELULA_SIZE
                linha = y // CELULA_SIZE
                if 0 <= coluna < 9 and 0 <= linha < 9:
                    selecionando = (linha, coluna)
            
            elif evento.type == pygame.KEYDOWN:
                if selecionando:
                    linha, coluna = selecionando
                    if evento.key == pygame.K_1:
                        tabuleiro[linha][coluna] = 1
                    elif evento.key == pygame.K_2:
                        tabuleiro[linha][coluna] = 2
                    elif evento.key == pygame.K_3:
                        tabuleiro[linha][coluna] = 3
                    elif evento.key == pygame.K_4:
                        tabuleiro[linha][coluna] = 4
                    elif evento.key == pygame.K_5:
                        tabuleiro[linha][coluna] = 5
                    elif evento.key == pygame.K_6:
                        tabuleiro[linha][coluna] = 6
                    elif evento.key == pygame.K_7:
                        tabuleiro[linha][coluna] = 7
                    elif evento.key == pygame.K_8:
                        tabuleiro[linha][coluna] = 8
                    elif evento.key == pygame.K_9:
                        tabuleiro[linha][coluna] = 9
                    elif evento.key == pygame.K_BACKSPACE:
                        tabuleiro[linha][coluna] = 0
        
        desenhar_tab(tabuleiro)
    
    pygame.quit()


jogo()