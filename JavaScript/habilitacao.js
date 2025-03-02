alert("Boas vindas ao nosso site!");
let nome = prompt("Qual o seu nome? ");
let idade = prompt("Qual a sua idade? ");

if(idade >= 18) {
    alert(`${nome} Parabens! Você pode tirar a habilitação!`);
}
else {
    alert(`${nome} Infelizmente, ainda não é possivel tirar a habilitação`);
}