let numeroSecreto = gerarNumeroAleatorio();

function exibirTextoTela(tag, texto){
let campo = document.querySelector(tag);
campo.innerHTML = texto;
}

exibirTextoTela('h1', 'Jogo do número secreto')
exibirTextoTela('p', 'Escolha um númer  o entre 1 e 10')

function verificarChute(){
    console.log(numeroSecreto);
}

function gerarNumeroAleatorio(params) {
   return parseInt(Math.random() * 10 + 1);
    
}