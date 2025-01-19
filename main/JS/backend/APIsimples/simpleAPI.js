const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("Welcome to the API");
});

app.get("/users", (req, res) => {
  res.json([
    { id: 1, name: "Gabriel" },
    { id: 2, name: "Bianca" },
    { id: 3, name: "Marcos" },
  ]);
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});

// Example request: GET http://localhost:3000/users
