const express = require("express");
const { engine } = require("express-handlebars");
const bodyparser = require("body-parser");
const path = require("path");
const app = express();

const fakedata = [
  {
    id: 1,
    nome: "Pedro",
    endereco: "Rua João Butschardt 2",
    telefone: "99601-4651",
  },
  {
    id: 2,
    nome: "Adriano",
    endereco: " Rua 28 de Agosto 1700",
    telefone: "3373-0203",
  },
];

/*Configura a engine (motor) do express para utilizar o handlebars*/
app.use(bodyparser.urlencoded({ extended: false }));
app.set("view engine", "handlebars");
app.engine("handlebars", engine());

/*disponobilizado acesso para as bibliotecas estaticas do boostrap e jquery*/
app.use(
  "/css",
  express.static(path.join(__dirname, "node_modules/bootstrap/dist/css"))
);
app.use(
  "/js",
  express.static(path.join(__dirname, "node_modules/bootstrap/dist/js"))
);
app.use(
  "/js",
  express.static(path.join(__dirname, "node_modules/jquery/dist"))
);

app.get("/home", function (req, res) {
  res.render("index");
});

app.get("/clientes", function (req, res) {
  res.render("clientes", { listaClientes: fakedata });
});

app.get("/clientes/novo", function (req, res) {
  res.render("formcliente");
});

app.get("/clientes/alterar/:id", function (req, res) {
  let idcliente = req.params["id"];
  let umcliente = fakedata.find((o) => o.id == idcliente);
  res.render("formcliente", { cliente: umcliente });
});

app.post("/clientes/save", function (req, res) {
  let clienteantigo = fakedata.find((o) => o.id == req.body.id);
  if (clienteantigo != undefined) {
    /*ALTERAR*/
    clienteantigo.nome = req.body.nome;
    clienteantigo.endereco = req.body.endereco;
    clienteantigo.telefone = req.body.telefone;
    clienteantigo.sexo = req.body.sexo;
  } else {
    /*INCLUIR */
    let maxid = Math.max(...fakedata.map((o) => o.id));
    if (maxid == -Infinity) {
      maxid = 0;
    }

    let novocliente = {
      nome: req.body.nome,
      endereco: req.body.endereco,
      sexo: req.body.sexo,
      telefone: req.body.telefone,
      id: maxid + 1,
    };
    fakedata.push(novocliente);
  }

  res.redirect("/clientes");
});

app.listen(3000, () => {
  console.log("Server Online - http://localhost:3000/home");
});
