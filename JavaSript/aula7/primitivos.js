// string, number, undefined, null, boolean, symbol.
const nome = "Diogo"; //string
const num1 = 10; //number
const num2 = 10.52;//number
let nomeAluno; //undefined = Não aponta pra local nenhum na memória
let sobrenomeAluno = null; // Nulo -> não aponta pra local nenhum na memória, é pra quando o usuário não seleciona nada.
const boolean = true; // apenas dois valores : true or false. (lógico)
const aprovado = true;

/*const a = [1, 2];
const b = a;

console.log(a, b);

b.push(3);
console.log(a, b)*/

let a = 2;
const b = a;

a = 3;

// b sempre vai pegar o valor original


console.log(a, b) //3,2