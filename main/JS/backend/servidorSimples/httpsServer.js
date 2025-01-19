const https = require("https");
const selfsigned = require("selfsigned");
const express = require("express");

const app = express();

app.get("/", (req, res) => {
  res.send("Servidor seguro com HTTPS!");
});

// Gere os certificados dinamicamente
const attrs = [{ name: "commonName", value: "localhost" }];
const pems = selfsigned.generate(attrs, { days: 365 });

// Crie o servidor HTTPS
https
  .createServer({ key: pems.private, cert: pems.cert }, app)
  .listen(3000, () => {
    console.log("Servidor HTTPS rodando em https://localhost:3000");
  });
