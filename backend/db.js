const mongoose = require("mongoose");

const connectDB = async () => {
  try {
    await mongoose.connect("bharathkumar08052004@gmail.com");

    console.log("MongoDB connected ✅");
  } catch (err) {
    console.log("DB connection error ❌", err);
  }
};

module.exports = connectDB;