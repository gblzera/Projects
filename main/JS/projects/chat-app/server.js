const express = require("express");
const http = require("http");
const WebSocket = require("ws");

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

app.use(express.static("public"));

wss.on("connection", (ws) => {
  console.log("Novo cliente conectado");

  // Salva o nome de usuário ao receber a primeira mensagem
  ws.on("message", (message) => {
    const data = JSON.parse(message);
    if (data.type === "identification") {
      ws.username = data.username;
      console.log(`${ws.username} entrou no chat`);
      ws.send(
        JSON.stringify({ type: "info", message: `Bem-vindo, ${ws.username}!` })
      );
      return;
    }

    // Envia a mensagem para todos os clientes conectados
    if (data.type === "message") {
      const fullMessage = `${ws.username}: ${data.message}`;
      console.log(fullMessage);

      wss.clients.forEach((client) => {
        if (client.readyState === WebSocket.OPEN) {
          client.send(
            JSON.stringify({ type: "message", message: fullMessage })
          );
        }
      });
    }
  });

  ws.on("close", () => {
    console.log(`${ws.username || "Um cliente"} desconectou-se`);
  });
});

server.listen(8080, () => {
  console.log("Servidor WebSocket está rodando na porta 8080");
});
