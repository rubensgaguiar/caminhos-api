const express = require("express");

const PORT = process.env.POST || 8080;

const app = express();

app.get("/login", (req, res) => {
  res.json({ message: "Você logou!" });
});

app.listen(PORT, () => {
  console.log(`Server is running on ${PORT}`);
});
