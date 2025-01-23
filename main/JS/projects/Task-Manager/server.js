const express = require("express");
const mongoose = require("mongoose");

const app = express();
const PORT = process.env.PORT || 3000;

// Conexão com o MongoDB
mongoose
  .connect("mongodb://localhost:27017/tarefas")
  .then(() => console.log("Conectado ao MongoDB"))
  .catch((err) => console.error("Erro ao conectar ao MongoDB:", err));

app.use(express.json());

const tasksRouter = require(`./routes/tasks`);
app.use("/tasks", tasksRouter);

app.listen(PORT, () => {
  console.log(`http://localhost:${PORT}/task`);
});
