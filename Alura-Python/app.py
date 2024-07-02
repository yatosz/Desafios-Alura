#!/usr/bin/env python3

import os

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

def finalizar_app():
    print('Finalizando o app...\n')

def escolhe_opcao():
      escolha_opcao = int(input("Escolha uma opção: "))
      #  escolha_opcao = int(escolha_opcao)
      match escolha_opcao:
            case 1:
                  print("Cadastrar restaurante")

            case 2:
                  print("Cadastrar restaurantes")

            case 3:
                  print("Ativar restaurante")

            case 4:
                  #os.system("cls") windows
                  os.system("clear") # mac / linux
                  finalizar_app()
      
            case _:
                  print("\nOpção inválida!\n")

def main():
    nome_programa()
    mostra_opcoes()
    escolhe_opcao()

if __name__ == "__main__":
    main()