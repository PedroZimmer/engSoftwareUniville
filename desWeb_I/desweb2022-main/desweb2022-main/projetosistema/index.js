const express = require('express');
const { engine } = require('express-handlebars');
const { create } = require('express-handlebars');
const bodyparser = require('body-parser');
const path = require('path');
const app = express();

const fakedata = [
    {
        id: 1,
        nome: 'Zezinho',
        endereco: 'Rua lalalal 100',
        telefone: '5555-1234',
        cancelado: 'nao'
    },
    {
        id: 2,
        nome: 'Huguinho',
        endereco: 'Rua lululul 200',
        telefone: '5555-4321',
        cancelado: 'sim'
    }
];
/*Configura a engine (motor) do express para utilizar o handlebars */
app.use(bodyparser.urlencoded({extended: false}));
app.set('view engine','handlebars');
app.engine('handlebars', engine());

create({}).handlebars.registerHelper('checked', function(value, test) {
    if (value == undefined) return '';
    return value==test ? 'checked' : '';
});
/*disponibilizando acesso para as bibliotecas estaticas do bootstrap e jquery */
app.use('/css', express.static(path.join(__dirname, 'node_modules/bootstrap/dist/css')));
app.use('/js', express.static(path.join(__dirname, 'node_modules/bootstrap/dist/js')));
app.use('/js', express.static(path.join(__dirname, 'node_modules/jquery/dist')));
app.use('/public', express.static(path.join(__dirname, 'public')));

app.get('/', function(req,res){
    //res.send("<h1>eu nao acredito</h1>");
    res.render('index');
});

app.get('/clientes/delete/:id', function(req,res){
    let umcliente = fakedata.find(o => o.id == req.params['id']);
    let index = fakedata.indexOf(umcliente);
    if (index > -1){
        fakedata.splice(index,1);
    }
    res.render('cliente/clientes',{data: fakedata});
});


app.get('/clientes/novo', function(req,res){
    res.render('cliente/formcliente');
});

app.get('/clientes/alterar/:id', function(req,res){
    let idcliente = req.params['id'];
    let umcliente = fakedata.find( o => o.id == idcliente);
    
    res.render('cliente/formcliente', {cliente: umcliente});
    
});



app.post('/clientes/save', function(req,res){
    let clienteantigo = fakedata.find(o => o.id == req.body.id);

    if(clienteantigo != undefined){
        /*ALTERAR */
        clienteantigo.nome = req.body.nome;
        clienteantigo.endereco = req.body.endereco;
        clienteantigo.telefone = req.body.telefone;
        clienteantigo.sexo = req.body.sexo;
        clienteantigo.cancelado = req.body.cancelado;
    }else{
        /*INCLUIR */
        let maxid = Math.max(...fakedata.map( o => o.id));
        if (maxid == -Infinity) maxid = 0;

        let novocliente = {
            nome: req.body.nome,
            endereco: req.body.endereco,
            sexo: req.body.sexo,
            telefone: req.body.telefone,
            id: maxid + 1,
            cancelado: req.body.cancelado
        };
        fakedata.push(novocliente);
    }
    res.redirect("/clientes");
});


app.get('/clientes', function(req,res){
    //res.send("<h1>eu nao acredito</h1>");
    res.render('cliente/clientes', {listaclientes: fakedata});
});

/*inicialização da aplicação NodeJS + Express */
app.listen(3000, () =>{
    console.log('Server online - http://localhost:3000/');
});
