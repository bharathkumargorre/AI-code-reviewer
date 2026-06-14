const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

// Fake login (NO MongoDB)
app.post("/login", (req, res) => {
  const { username, password } = req.body;

  if (username === "admin" && password === "1234") {
    return res.json({
      success: true,
      token: "demo-token-123"
    });
  }

  return res.status(400).json({
    success: false,
    message: "Invalid credentials"
  });
});

app.get("/dashboard-data", (req, res) => {
  res.json({
    message: "Dashboard loaded",
    users: 10,
    revenue: 5000,
    activeSessions: 3
  });
});

app.listen(5000, () => {
  console.log("Server running on port 5000");
});