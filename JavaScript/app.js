//Baixei a extenssão (para ser um meu servidor local)

alert('Boas vindas ao jogo do número secreto'); //Serve para mostrar uma mensagem ao usuario. O ";" não é obrigátorio ultilizar o ";"
let numeroSecreto = 5; //let refere-se a variavel (no caso chamo a variavel "let" e logo apos ela passo o nome da variavel e depois do = passo um valor)
console.log(numeroSecreto); //Usa o console.log para ver internamente atraves do log da pagina se as funções estão funcionando corretamente ou não
let chute;
let tentativas = 1; //Icremento de tentativas

// Enquanto o chute não for igual ao numero secreto faça...
while (chute != numeroSecreto) {
    chute = prompt('Escolha um numero entre 1 e 30'); //Recebe um valor digitado pelo usuario

    if (chute == numeroSecreto) {
        alert(`Isso ai! Você descobriu o número secreto ${numeroSecreto} com ${tentativas} tentativas`); //Para concactenar é necessario usar ` (acentuação) ao invés de aspas simples ou duplas
    }
    else {
        if(chute > numeroSecreto) {
            alert(`O número secreto é menor que ${chute}`);
        }
        else {
            alert(`O número secreto é maior que ${chute}`);            
        }
        tentativas++;    
    }
}