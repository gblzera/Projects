const board = document.getElementById("board");
const status = document.getElementById("status");
const restart = document.getElementById("restart");

let currentPlayer = "X";
let gameActive = true;
let gameState = Array(9).fill(null);

const winningConditions = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6],
];

function handleCellClick(event) {
  const cell = event.target;
  const cellIndex = cell.getAttribute("data-index");

  if (gameState[cellIndex] || !gameActive) return;

  gameState[cellIndex] = currentPlayer;
  cell.textContent = currentPlayer;
  cell.classList.add("taken");

  if (checkWin()) {
    status.textContent = `Player ${currentPlayer} wins!`;
    highLightWinningCells();
    gameActive = false;
    disableCells(); // Desabilita as células após o término do jogo
    return;
  }

  if (!gameState.includes(null)) {
    status.textContent = "It's a draw!";
    gameActive = false;
    disableCells(); // Desabilita as células após o término do jogo
    return;
  }

  currentPlayer = currentPlayer === "X" ? "O" : "X";
  status.textContent = `Player ${currentPlayer}, it's your turn.`;
}

function checkWin() {
  return winningConditions.some((condition) => {
    const [a, b, c] = condition;
    if (
      gameState[a] &&
      gameState[a] === gameState[b] &&
      gameState[a] === gameState[c]
    ) {
      condition.forEach((index) => {
        document
          .querySelector(`.cell[data-index='${index}']`)
          .classList.add("winning");
      });
      return true;
    }
    return false;
  });
}

function disableCells() {
  Array.from(board.children).forEach((cell) => {
    cell.removeEventListener("click", handleCellClick); // Remove o evento de clique
  });
}

function restartGame() {
  gameState.fill(null);
  gameActive = true;
  currentPlayer = "X";
  status.textContent = "Player X, it's your turn.";

  Array.from(board.children).forEach((cell) => {
    cell.textContent = "";
    cell.classList.remove("taken", "winning");
    cell.addEventListener("click", handleCellClick); // Re-adiciona o evento de clique
  });
}

function initializeBoard() {
  board.innerHTML = "";
  gameState.forEach((_, index) => {
    const cell = document.createElement("div");
    cell.classList.add("cell");
    cell.setAttribute("data-index", index);
    cell.addEventListener("click", handleCellClick);
    board.appendChild(cell);
  });
}

restart.addEventListener("click", restartGame);
initializeBoard();
