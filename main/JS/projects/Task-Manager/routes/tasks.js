const express = require("express");
const task = require("../models/tasks");
const router = express.Router();

// Criar uma task nova
router.post("/", async (req, res) => {
  const task = new Task(req.body);
  try {
    await task.save();
    res.status(201).send(task);
  } catch (error) {
    res.status(400).send(error);
  }
});

// Obter todas as tasks
router.get("/", async (req, res) => {
  try {
    const tasks = await Task.find();
    res.send(tasks);
  } catch (error) {
    res.status(500).send(error);
  }
});

// Att uma task
router.patch("/:id", async (req, res) => {
  try {
    const task = await Task.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!task) return res.status(404).send("Task não encontrada");
    res.send(task);
  } catch (error) {
    res.status(400).send(error);
  }
});

// Deletar uma task

router.delete("/:id", async (req, res) => {
  try {
    const task = await Task.findByIdAndDelete(req.params.id);
    if (!task) return res.status(404).send("Task não encontrada");
    res.send(task);
  } catch (error) {
    res.status(500).send(error);
  }
});

module.exports = router;
