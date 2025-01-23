const mongoose = require("mongoose");

const taskSchema = new mongoose.Schema({
  titulo: { type: String, required: true },
  descricao: { typoe: String },
  data_criacao: { type: Date, default: Date.now },
  data_conclusao: { type: Date },
  prioridade: {
    type: String,
    enum: ["baixa", "media", "alta"],
    default: "baixa",
  },
  status: {
    type: String,
    enum: ["pendente", "em_andamento", "concluida"],
    default: "pendente",
  },
});

module.exports = mongoose.model("Tasks", taskSchema);
