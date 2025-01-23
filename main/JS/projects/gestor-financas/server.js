const express = require("express");
const mongoose = require("mongoose");
const path = require("path");

// Iniciar o aplicativo Express
const app = express();
const port = 5000;

// Conectar ao MongoDB (certifique-se de configurar o URI correto)
mongoose
  .connect("mongodb://localhost/gestor-financas", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("Conectado ao MongoDB"))
  .catch((err) => console.log("Erro ao conectar ao MongoDB:", err));

// Configurar a pasta para arquivos estáticos (CSS, imagens, etc.)
app.use(express.static(path.join(__dirname, "public")));

// Middleware para analisar dados de formulários
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Rota principal
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

// API para buscar transações
app.get("/api/transacoes", (req, res) => {
  // Aqui você pode pegar as transações do MongoDB e enviar
  const transacoes = [
    { tipo: "receita", valor: 200 },
    { tipo: "despesa", valor: 100 },
  ];
  res.json(transacoes);
});

// Iniciar o servidor
app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
