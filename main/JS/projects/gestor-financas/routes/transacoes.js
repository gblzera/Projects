// routes/transacoes.js
const express = require("express");
const router = express.Router();
const Transacao = require("../models/Transacao");

// Criar nova transação
router.post("/add", async (req, res) => {
  const { tipo, descricao, valor, categoria } = req.body;

  try {
    const novaTransacao = new Transacao({ tipo, descricao, valor, categoria });
    await novaTransacao.save();
    res.status(201).json(novaTransacao);
  } catch (err) {
    res.status(500).json({ message: "Erro ao adicionar transação" });
  }
});

// Obter todas as transações
router.get("/", async (req, res) => {
  try {
    const transacoes = await Transacao.find();
    res.status(200).json(transacoes);
  } catch (err) {
    res.status(500).json({ message: "Erro ao buscar transações" });
  }
});

module.exports = router;
