// first of all, import express
const express = require("express");
const app = express();
const port = 3000;

// route to add
app.get("/add", (req, res) => {
  const { num1, num2 } = req.query;

  // Validate if numbers sent are valid
  if (!num1 || !num2) {
    return res.status(400).json({ error: "Please enter two numbers" });
  }

  const number1 = parseFloat(num1);
  const number2 = parseFloat(num2);

  if (isNaN(number1) || isNaN(number2)) {
    return res
      .status(400)
      .json({ error: "Both num1 and num2 must be numbers" });
  }

  const result = number1 + number2;
  res.json({ result });
});

// initialize server
app.listen(port, () => {
  console.log(`Server is running on port https://localhost:${port}`);
});

//erro, verificar
