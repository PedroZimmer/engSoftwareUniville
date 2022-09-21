let salario = 10
let idade = 10

//let resp = prompt("Informe sua data de nascimento", "dd/mm/aa")
//console.log(resp)


window.document.write("<p>EU N ACREDITO</p>")
window.document.write("pior q é vdd")


//TIPO NUMBER
a = 10
console.log(a + " " + typeof(a))
a = 20.5
console.log(a + " " + typeof(a))

//TIPO LÓGICO - boolean
a = true
console.log(a + " " + typeof(a))

//STRING
a = "Como assim a mesma variavel"
console.log(a + " " + typeof(a))

//ARRAY - object
a = ['posicao 1', 'posicao 2']
console.log(a[0] + " " + typeof(a))
a[0] = 'outra coisa'
console.log(a[0] + " " + typeof(a))

a = new Array()
a[0] = 'outra coisa'
console.log(a + " " + typeof(a))

a = new Object()
a.idade = 10
console.log(a.idade + " " + typeof(a))

//DECLARAÇÃO

function botao1() {
    alert("Botao foi clicado")
}

let x = 43
console.log(x == 43)