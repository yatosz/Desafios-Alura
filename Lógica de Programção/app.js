let titulo = document.querySelector('h1');
titulo.innerHTML = 'Hora do Desafio';

let paragrafo = document.querySelector('p');
paragrafo.innerHTML = 'Escolha um número entre 1 e 10';

function exibirNoConsole(){
    console.log('O botão foi clicado!');

}

function exibirAlerta(){
    alert('Eu Amo JS');
}

function exibirPrompt(){
    let nomeCidade = prompt('Digite o nome de uma cidade do Brasil');
    alert(`Estive em ${nomeCidade} e lembrei de você`);
}

function somaResultado(){
    let primeiroNumero = parseInt(prompt('Informe o primeiro número: '));
    let segundoNumero = parseInt(prompt('Informe o segundo número: '));

    let resultadoSoma = primeiroNumero + segundoNumero;

    alert(`${primeiroNumero} + ${segundoNumero} = ${resultadoSoma}`);
}