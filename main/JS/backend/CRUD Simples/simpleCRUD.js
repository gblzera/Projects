const express = require("express");
const app = express();

app.use(express.json());

let users = [];

app.post("/users", (req, res) => {
  const user = req.body;
  users.push(user);
  res.status(201).send("User added successfull!");
});

app.get("/users", (req, res) => {
  res.json(users);
});

app.delete("/users/:id", (req, res) => {
  const id = parseInt(req.params.id);
  users = users.filter((u) => u.id !== id);
  res.send("User deleted successfully!");
});

app.listen(3000, () => {
  console.log("API listening on port 3000");
});

//verificar estudos sobre, algo de errado.
