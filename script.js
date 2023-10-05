document.addEventListener("DOMContentLoaded", function () {
    const board = document.getElementById("board");
    const message = document.getElementById("message");
    const restartButton = document.getElementById("restart-button");

    let currentPlayer = "X";
    let cells = ["", "", "", "", "", "", "", "", ""];

    function checkWinner() {
        const winPatterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
            [0, 4, 8], [2, 4, 6]             // Diagonals
        ];

        for (const pattern of winPatterns) {
            const [a, b, c] = pattern;
            if (cells[a] && cells[a] === cells[b] && cells[a] === cells[c]) {
                return cells[a];
            }
        }

        if (cells.every(cell => cell !== "")) {
            return "draw";
        }

        return null;
    }

    function handleCellClick(index) {
        if (cells[index] === "" && !checkWinner()) {
            cells[index] = currentPlayer;
            render();
            currentPlayer = currentPlayer === "X" ? "O" : "X";
        }
    }

    function render() {
        board.innerHTML = "";
        cells.forEach((cell, index) => {
            const cellElement = document.createElement("div");
            cellElement.classList.add("cell");
            cellElement.textContent = cell;
            cellElement.addEventListener("click", () => handleCellClick(index));
            board.appendChild(cellElement);
        });

        const winner = checkWinner();
        if (winner) {
            if (winner === "draw") {
                message.textContent = "It's a draw!";
            } else {
                message.textContent = `Player ${winner} wins!`;
            }
        } else {
            message.textContent = `Player ${currentPlayer}'s turn`;
        }
    }

    restartButton.addEventListener("click", () => {
        cells = ["", "", "", "", "", "", "", "", ""];
        currentPlayer = "X";
        render();
    });

    render();
});
