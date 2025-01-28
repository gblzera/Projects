import pygame

LARGURA, ALTURA = 480, 480
TAMANHO_CELULA = 60
CORES = [(255, 206, 158), (209, 139, 71)]  # Branco e marrom
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Xadrez")

pecas = {
    "bP": pygame.image.load("assets/peao_branco.png"),
    "bT": pygame.image.load("assets/rook_branca.png"),
    "bC": pygame.image.load("assets/cavalo_branco.png"),
    "bB": pygame.image.load("assets/bishop_branca.png"),
    "bQ": pygame.image.load("assets/rainha_branca.png"),
    "bK": pygame.image.load("assets/rei_branco.png"),
    "pP": pygame.image.load("assets/peao_preto.png"),
    "pT": pygame.image.load("assets/rook_preta.png"),
    "pC": pygame.image.load("assets/cavalo_preto.png"),
    "pB": pygame.image.load("assets/bishop_preta.png"),
    "pQ": pygame.image.load("assets/rainha_preta.png"),
    "pK": pygame.image.load("assets/rei_preto.png"),
}

for key in pecas:
    pecas[key] = pygame.transform.scale(pecas[key], (TAMANHO_CELULA, TAMANHO_CELULA))

tabuleiro = [
    ["pT", "pC", "pB", "pQ", "pK", "pB", "pC", "pT"],
    ["pP", "pP", "pP", "pP", "pP", "pP", "pP", "pP"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
    ["bT", "bC", "bB", "bQ", "bK", "bB", "bC", "bT"],
]

turno = "branco"  

def desenhar_tabuleiro():
    for linha in range(8):
        for coluna in range(8):
            cor = CORES[(linha + coluna) % 2]
            pygame.draw.rect(screen, cor, (coluna * TAMANHO_CELULA, linha * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))

def desenhar_pecas():
    for linha in range(8):
        for coluna in range(8):
            peca = tabuleiro[linha][coluna]
            if peca != "-":  # Se houver uma peça
                screen.blit(pecas[peca], (coluna * TAMANHO_CELULA, linha * TAMANHO_CELULA))

# Função para calcular movimentos válidos de peões
def movimentos_peao(peca, linha, coluna):
    movimentos = []
    direcao = -1 if peca[0] == "b" else 1  # Direção para brancas (-1) e pretas (+1)
    # Movimento para frente
    if tabuleiro[linha + direcao][coluna] == "-":
        movimentos.append((linha + direcao, coluna))
        # Movimento inicial de dois passos
        if (linha == 6 and peca[0] == "b") or (linha == 1 and peca[0] == "p"):
            if tabuleiro[linha + 2 * direcao][coluna] == "-":
                movimentos.append((linha + 2 * direcao, coluna))
    # Capturas diagonais
    for dc in [-1, 1]:
        if 0 <= coluna + dc < 8 and tabuleiro[linha + direcao][coluna + dc] != "-":
            if tabuleiro[linha + direcao][coluna + dc][0] != peca[0]:  # Peça inimiga
                movimentos.append((linha + direcao, coluna + dc))
    return movimentos

# Função para calcular movimentos válidos de torres
def movimentos_torre(peca, linha, coluna):
    movimentos = []
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Movimentos para cima, baixo, esquerda, direita
    for dx, dy in direcoes:
        x, y = linha, coluna
        while True:
            x += dx
            y += dy
            if 0 <= x < 8 and 0 <= y < 8:
                if tabuleiro[x][y] == "-":
                    movimentos.append((x, y))
                elif tabuleiro[x][y][0] != peca[0]:  # Peça inimiga
                    movimentos.append((x, y))
                    break
                else:  # Peça aliada
                    break
            else:
                break
    return movimentos

# Função para calcular movimentos válidos de bispos
def movimentos_bispo(peca, linha, coluna):
    movimentos = []
    direcoes = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Movimentos diagonais
    for dx, dy in direcoes:
        x, y = linha, coluna
        while True:
            x += dx
            y += dy
            if 0 <= x < 8 and 0 <= y < 8:
                if tabuleiro[x][y] == "-":
                    movimentos.append((x, y))
                elif tabuleiro[x][y][0] != peca[0]:  # Peça inimiga
                    movimentos.append((x, y))
                    break
                else:  # Peça aliada
                    break
            else:
                break
    return movimentos

def movimentos_rainha(peca, linha, coluna):
    return movimentos_torre(peca, linha, coluna) + movimentos_bispo(peca, linha, coluna)

# Função para calcular movimentos válidos de cavalo
def movimentos_cavalo(peca, linha, coluna):
    movimentos = []
    direcoes = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
    for dx, dy in direcoes:
        x, y = linha + dx, coluna + dy
        if 0 <= x < 8 and 0 <= y < 8:
            if tabuleiro[x][y] == "-" or tabuleiro[x][y][0] != peca[0]:  # Peça vazia ou inimiga
                movimentos.append((x, y))
    return movimentos

# Função para calcular movimentos válidos de rei
def movimentos_rei(peca, linha, coluna):
    movimentos = []
    direcoes = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in direcoes:
        x, y = linha + dx, coluna + dy
        if 0 <= x < 8 and 0 <= y < 8:
            if tabuleiro[x][y] == "-" or tabuleiro[x][y][0] != peca[0]:  # Peça vazia ou inimiga
                movimentos.append((x, y))
    return movimentos

def movimentos_validos(peca, linha, coluna):
    if peca[1] == "P":
        return movimentos_peao(peca, linha, coluna)
    elif peca[1] == "T":
        return movimentos_torre(peca, linha, coluna)
    elif peca[1] == "B":
        return movimentos_bispo(peca, linha, coluna)
    elif peca[1] == "Q":
        return movimentos_rainha(peca, linha, coluna)
    elif peca[1] == "C":
        return movimentos_cavalo(peca, linha, coluna)
    elif peca[1] == "K":
        return movimentos_rei(peca, linha, coluna)
    return []

running = True
peca_selecionada = None
movimentos = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            coluna, linha = x // TAMANHO_CELULA, y // TAMANHO_CELULA
            if peca_selecionada:  # Tentar mover a peça
                if (linha, coluna) in movimentos:
                    tabuleiro[linha][coluna] = peca_selecionada
                    tabuleiro[pos_peca[0]][pos_peca[1]] = "-"
                    turno = "preto" if turno == "branco" else "branco"  # Alternar turno
                peca_selecionada = None
                movimentos = []
            else:  # Selecionar uma peça
                peca_selecionada = tabuleiro[linha][coluna]
                if peca_selecionada != "-" and ((turno == "branco" and peca_selecionada[0] == "b") or (turno == "preto" and peca_selecionada[0] == "p")):
                    movimentos = movimentos_validos(peca_selecionada, linha, coluna)
                    pos_peca = (linha, coluna)

    screen.fill((255, 255, 255))  
    desenhar_tabuleiro()
    desenhar_pecas()

    for mov in movimentos:
        pygame.draw.rect(screen, (0, 255, 0), (mov[1] * TAMANHO_CELULA, mov[0] * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA), 3)
    pygame.display.flip()

pygame.quit()
