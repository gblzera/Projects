document
  .getElementById("form-transacao")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const descricao = document.getElementById("descricao").value;
    const valor = parseFloat(document.getElementById("valor").value);
    const tipo = document.getElementById("tipo").value;

    // Enviar os dados para o servidor
    fetch("/api/transacoes", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ descricao, valor, tipo }),
    })
      .then((response) => response.json())
      .then(() => atualizarGrafico())
      .catch((error) => console.error("Erro ao adicionar transação:", error));
  });

function atualizarGrafico() {
  fetch("/api/transacoes")
    .then((response) => response.json())
    .then((data) => {
      let receitas = 0;
      let despesas = 0;

      data.forEach((transacao) => {
        if (transacao.tipo === "receita") {
          receitas += transacao.valor;
        } else {
          despesas += transacao.valor;
        }
      });

      grafico.data.datasets[0].data = [receitas, despesas];
      grafico.update();
    })
    .catch((error) => console.error("Erro ao carregar as transações:", error));
}

// Inicializar o gráfico
const ctx = document.getElementById("grafico").getContext("2d");
const grafico = new Chart(ctx, {
  type: "bar",
  data: {
    labels: ["Receitas", "Despesas"],
    datasets: [
      {
        label: "Total",
        data: [0, 0], // Inicializar com valores zerados
        backgroundColor: ["green", "red"],
      },
    ],
  },
});
