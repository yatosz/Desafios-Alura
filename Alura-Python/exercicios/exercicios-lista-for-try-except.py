#!/usr/bin/env python3

import os
# 1 - Crie uma lista para cada informação a seguir:

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_nomes = ['Igor', 'Hanna', 'Rafael', "Lais"]

lista_anos = ['1999', '2024']

def listar_numeros():
    print('\nOrdem crescente: \n')
    lista_impares = []
    for numero in range(0, 10, 1):
        print(f'.{numero}\n')

        if(numero % 2 != 0):
            lista_impares.append(numero)
    
    soma_impares = sum(lista_impares) 
    print(f'soma dos números ímpares: {soma_impares} \n\n')
    
    #######-----ordem decrescente-----#######
    print('\nOrdem decrescente: \n')
    for numero in range(10, 0, -1):
        print(f'.{numero}\n')

def listar_nomes():
    print('\nlistando nomes: \n')
    for nome in lista_nomes:
        print(f'.{nome}\n')

def listar_anos():
    for lista in lista_anos:
        print(f'.{lista}\n')

def loop_tabuada():
    print('\n###---Tabuada---###\n')
    numero_inserido = int(input('Digite o valor desejado: '))

    for numero in range(1, 11, 1):
        print(f'{numero_inserido} x {numero} = {numero_inserido * numero}')

def calcular_soma_elementos():
    print('\n###---Calcular soma dos Elementros---###\n')
    
    lista_numeros = [1, 2, 3, 4, 5]
    total_soma = 0
        
    for numero in lista_numeros:
        try:
            total_soma += numero

        except ValueError:
            print('Erro: Digite um número válido')

        except Exception as e:
            print(f'ocorreu um erro inesperado {e}')

    print(f'Calculo total: {total_soma}')

def calcular_media_lista():
    print('\n###---Calculo Media Lista---###\n')
    lista_numeros = [10, 15, 30, 45]

    soma_total = 0
    try:
        for numero in lista_numeros:
            print(f'valores: {numero}')
            soma_total += numero 

        media = (soma_total / len(lista_numeros))
        print(f'\nmédia dos valores: {media} \n')

    except ZeroDivisionError:
        print("Erro: Não é possível divisão por zero!")

    except Exception  as e:
        print(f'Erro: ocorreu um erro inesperado! {e}')

if __name__ == "__main__":
    listar_numeros()
    listar_nomes()
    listar_anos()
    loop_tabuada()
    calcular_soma_elementos()
    calcular_media_lista()