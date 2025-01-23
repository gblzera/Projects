// models/Transacao.js
const mongoose = require("mongoose");

const TransacaoSchema = new mongoose.Schema({
  tipo: {
    type: String, // 'receita' ou 'despesa'
    required: true,
  },
  descricao: {
    type: String,
    required: true,
  },
  valor: {
    type: Number,
    required: true,
  },
  data: {
    type: Date,
    default: Date.now,
  },
  categoria: String, // Ex: 'Alimentação', 'Lazer'
});

module.exports = mongoose.model("Transacao", TransacaoSchema);
