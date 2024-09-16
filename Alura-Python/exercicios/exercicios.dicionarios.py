#!/usr/bin/env python3


informacoes_pessoas = [{'nome':'Igor Vidal', 'idade':24, 'Cidade':'DV'},
                       {'nome': 'Hanna', 'idade':24, 'Cidade':'DV'},
                       {'nome': 'Nancy', 'idade': 2, 'Cidade':'Toledo'}]

print(informacoes_pessoas)

informacoes_pessoas[0]['idade'] = 25
informacoes_pessoas[0]['Profissão'] = 'Medico'

del informacoes_pessoas[0]['Cidade']
print()
print(informacoes_pessoas)


###---Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.---###
print('\n\n')
print("Números Quadrados: ")
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)


##---Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário | 
# Alterei algumas coisas e deixei mais interessante.---###

print("\n\nCompra de Veiculos, informe qual a sua escolha: Moto ou Carro: \n")

variavel_pesquisada = input("Informe o Modelo do Veiculo: ")

Veiculos = [{'Carro':'Camaro', 'Cor':'Azul'},
          {'Carro':'Mustang', 'Cor':'Preto'},
          {'Moto':'Yamaha', 'Cor':'Vermelha'}]

for Veiculo in Veiculos:
    if variavel_pesquisada in Veiculo:
        print(f'\nA Chave {Veiculo} está disponível para Compra')



###---Escreva um código que conte a frequência de 
# cada palavra em uma frase utilizando um dicionário.---###
print('\n\n')
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)