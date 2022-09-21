const express = require("express");
const { engine } = require("express-handlebars");
const { create } = require("express-handlebars");
const bodyparser = require("body-parser");
const path = require("path");
const app = express();

const fakedata = [
  {
    id: 1,
    nome: "Pedro",
    endereco: "Rua João Butschardt 2",
    telefone: "99601-4651",
    email: "pedroxlzmm@gmail.com",
    nivel: "Sócio Torcedor",
    cpf: "123.456.798-00",
    cartao: "1234 4657 8912 3456",
    cvc: "147",
  },
  {
    id: 2,
    nome: "Adriano",
    endereco: " Rua 28 de Agosto 1700",
    telefone: "3373-0203",
    email: "adriano@fon.com",
    nivel: "Sócio Torcedor",
    cpf: "789.465.123-00",
    cartao: "9876 5432 1098 7654",
    cvc: "369",
  },
];

/*Configura a engine (motor) do express para utilizar o handlebars*/
app.use(bodyparser.urlencoded({ extended: false }));
app.set("view engine", "handlebars");
app.engine("handlebars", engine());

create({}).handlebars.registerHelper("checked", function (value, test) {
  if (value == undefined) return "";
  return value == test ? "checked" : "";
});

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
app.use("/public", express.static(path.join(__dirname, "public")));

app.get("/home", function (req, res) {
  res.render("index");
});

app.get('/clientes/delete/:id' , function(req,res){
  let umcliente = fakedata.find(o => o.id == req.params['id']);
  let index = fakedata.indexOf (umcliente);
  if (index > -1) {
    fakedata.splice(index,1)
  }
  res.render('cliente/clientes', {data: fakedata})
})

app.get("/planos", function (req, res) {
  res.render("planos");
});

app.get("/clientes", function (req, res) {
  res.render("cliente/clientes", { listaClientes: fakedata });
});

app.get("/clientes/novo", function (req, res) {
  res.render("cliente/formcliente");
});

app.get("/clientes/alterar/:id", function (req, res) {
  let idcliente = req.params["id"];
  let umcliente = fakedata.find((o) => o.id == idcliente);
  res.render("cliente/formcliente", { cliente: umcliente });
});

app.post("/clientes/save", function (req, res) {
  console.log(req.body);
  let clienteantigo = fakedata.find((o) => o.id == req.body.id);
  if (clienteantigo != undefined) {
    /*ALTERAR*/
    clienteantigo.nome = req.body.nome;
    clienteantigo.endereco = req.body.endereco;
    clienteantigo.telefone = req.body.telefone;
    clienteantigo.email = req.body.email;
    clienteantigo.nivel = req.body.nivel;
    clienteantigo.cpf = req.body.cpf;
    clienteantigo.cartao = req.body.cartao;
    clienteantigo.cvc = req.body.cvc;
  } else {
    /*INCLUIR */
    let maxid = Math.max(...fakedata.map((o) => o.id));
    if (maxid == -Infinity) {
      maxid = 0;
    }

    let novocliente = {
      nome: req.body.nome,
      endereco: req.body.endereco,
      telefone: req.body.telefone,
      email: req.body.email,
      nivel: req.body.nivel,
      cpf: req.body.cpf,
      cartao: req.body.cartao,
      cvc: req.body.cvc,
      id: maxid + 1,
    };
    fakedata.push(novocliente);
  }

  res.redirect("/clientes");
});

app.listen(3000, () => {
  console.log("Server Online - http://localhost:3000/home");
});
