//alert("socorro!!!");
/* comentario de bloco */
//declaração de variáveis
let salario = 10;
var idade = 10;

//let resp = confirm("Voce esta certo disso, posso perguntar?");
//console.log(resp);

//let resp = prompt("Informe sua data de nascimento", "dd/MM/aaaa");
//console.log(resp)

window.document.write("EU NAO ACREDITO!!!!");
document.write("Pior que é verdade...");

//TIPO NUMBER
a = 10;
console.log(a + " " + typeof(a));
a = 20.5;
console.log(a + " " + typeof(a));
//TIPO LÓGICO - boolean
a = true;
console.log(a + " " + typeof(a));
//String
a = "Como assim a mesma variável";
console.log(a + " " + typeof(a));
//Array - Object
a = ['posicao 1','posicao 2'];
console.log(a[0] + " " + typeof(a));
a[0] = "outra coisa";
console.log(a[0] + " " + typeof(a));

a = new Array();
a[0] = "outra coisa";
console.log(a + " " + typeof(a));

a = new Object();
a.idade = 10;
console.log(a.idade + " " + typeof(a));

//Declaração de uma função
function botao1(){
    let nome = document.getElementById("txtnome").value;
    alert(nome + ' O botão foi clicado');
}
//console.log("ANTES");
//botao1();
//console.log("DEPOIS");

let x = 43;
console.log(x == 43);
console.log(x == "43");
console.log(x == 67);
console.log(x == "67");

console.log(x === 43);
console.log(x === "43");