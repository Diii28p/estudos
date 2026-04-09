/*
Luiz Otávio Miranda tem 30 anos, pesa 84kg
tem 1.8 de altura e seu IMC é de 25.9259.
Luiz Otavio nasceu em 
*/

const nome = "Diogo"
const sobrenome = "de Melo"
const idade = 22;
const peso = 63;
const alturaEmM = 1.80;
let anoNascimento = 2026 - idade;

let imc = peso / (alturaEmM * alturaEmM);



console.log(nome, sobrenome, 'tem', idade, 'anos, pesa', peso, 'kg', 'tem', alturaEmM, 'de altura e seu IMC é de', imc)

console.log(nome, 'nasceu em', anoNascimento +'.')