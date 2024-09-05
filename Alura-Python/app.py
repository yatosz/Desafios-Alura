#!/usr/bin/env python3

import os


restaurantes = ['teste1', 'teste2']

def nome_programa():
      print("""Sabor Express
      
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
      
      """)

def mostra_opcoes():
      print("1. Cadastrar restaurante")
      print("2. Listar restaurante")
      print("3. Ativar restaurante")
      print("4. Sair\n")


def opcao_invalida():
      print("\nOpção inválida!\n")
      input("Digite uma tecla para voltar ao menu principal: ")
      main()

def cadastrar_novo_restaurante():
      os.system("clear")
      print("\nCadastro de novos restaurantes\n")
      nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
      restaurantes.append(nome_do_restaurante)
      print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
      input("Digite uma tecla para voltar ao menu principal\n")
      main()

def finalizar_app():
    print('Finalizando o app...\n')

def listar_restaurantes():
      os.system('clear')
      print('Listar restaurantes\n')

      for lista in restaurantes:
            print(f'.{lista}\n')

      input('Digite uma tecla para voltar ao menu principal')
      main()

def escolhe_opcao():
      try:
            escolha_opcao = int(input("Escolha uma opção: "))
            #  escolha_opcao = int(escolha_opcao)
            match escolha_opcao:
                  case 1:
                        cadastrar_novo_restaurante()

                  case 2:
                        listar_restaurantes()

                  case 3:
                        print("Ativar restaurante")

                  case 4:
                  #os.system("cls") windows
                        os.system("clear") # mac / linux
                        finalizar_app()

                  case _:
                        opcao_invalida()
            
      except:
             opcao_invalida()

def main():
    os.system("clear")
    nome_programa()
    mostra_opcoes()
    escolhe_opcao()

if __name__ == "__main__":
    main()