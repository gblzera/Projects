#include <stdio.h>

#define SIZE 7

// Função para inicializar o tabuleiro
void inicializarTabuleiro(int tabuleiro[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            // Posições válidas para peças
            if ((i == 0 && (j == 3)) ||
                (i == 1 && (j == 1 || j == 3 || j == 5)) ||
                (i == 2 && (j == 0 || j == 1 || j == 3 || j == 5 || j == 6)) ||
                (i == 3 && (j == 0 || j == 1 || j == 3 || j == 5 || j == 6)) ||
                (i == 4 && (j == 0 || j == 1 || j == 3 || j == 5 || j == 6)) ||
                (i == 5 && (j == 1 || j == 3 || j == 5)) ||
                (i == 6 && (j == 3))) {
                tabuleiro[i][j] = 1;  // Coloca a peça
            } else {
                tabuleiro[i][j] = 0;  // Espaços vazios
            }
        }
    }
}

// Função para imprimir o tabuleiro
void imprimirTabuleiro(int tabuleiro[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (tabuleiro[i][j] == 1)
                printf(" O ");
            else
                printf(" - ");
        }
        printf("\n");
    }
}

// Função para verificar se o movimento é válido
int movimentoValido(int tabuleiro[SIZE][SIZE], int x1, int y1, int x2, int y2) {
    // Verifica se a posição inicial e final estão dentro dos limites do tabuleiro e se o movimento é válido
    if (x1 >= 0 && x1 < SIZE && y1 >= 0 && y1 < SIZE && x2 >= 0 && x2 < SIZE && y2 >= 0 && y2 < SIZE) {
        if (tabuleiro[x1][y1] == 1 && tabuleiro[x2][y2] == 0) {
            // Verifica se a peça pulada está no meio
            int mx = (x1 + x2) / 2;
            int my = (y1 + y2) / 2;
            if (tabuleiro[mx][my] == 1) {
                return 1;
            }
        }
    }
    return 0;
}

// Função para realizar o movimento
void realizarMovimento(int tabuleiro[SIZE][SIZE], int x1, int y1, int x2, int y2) {
    // Realiza o movimento: move a peça e remove a peça pulada
    tabuleiro[x2][y2] = 1;
    tabuleiro[x1][y1] = 0;
    int mx = (x1 + x2) / 2;
    int my = (y1 + y2) / 2;
    tabuleiro[mx][my] = 0;
}

// Função para verificar se o jogo terminou
int jogoTerminado(int tabuleiro[SIZE][SIZE]) {
    int count = 0;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (tabuleiro[i][j] == 1) {
                count++;
            }
        }
    }
    return count == 1;  // Se restar apenas uma peça, o jogo terminou
}

int main() {
    int tabuleiro[SIZE][SIZE];
    inicializarTabuleiro(tabuleiro);
    int x1, y1, x2, y2;

    while (!jogoTerminado(tabuleiro)) {
        imprimirTabuleiro(tabuleiro);
        printf("Digite o movimento (x1 y1 x2 y2): ");
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

        if (movimentoValido(tabuleiro, x1, y1, x2, y2)) {
            realizarMovimento(tabuleiro, x1, y1, x2, y2);
        } else {
            printf("Movimento inválido! Tente novamente.\n");
        }
    }

    printf("Parabéns, você venceu!\n");
    return 0;
}
