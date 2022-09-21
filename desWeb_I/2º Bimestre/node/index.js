const express = require("express");
const { engine } = require("express-handlebars");
const bodyparser = require("body-parser");
const path = require("path");
const app = express();

app.set("view engine", "handlebars");
app.engine("handlebars", engine());

app.get("/", function (req, res) {
  res.send("<h1>eu nao acredito</h1>");
});

app.listen(3000, () => {
  console.log("Server online");
});
