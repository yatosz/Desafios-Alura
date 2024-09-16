#!/usr/bin/env python3

import os


restaurantes = [{'nome':'praca', 'categoria':'japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Sushi', 'categoria':'Japonês', 'ativo':False}]

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

def voltar_menu_principal():
      input("\nDigite uma tecla para voltar ao menu principal: ")
      main()

def opcao_invalida():
      print("\nOpção inválida!\n")
      voltar_menu_principal()

def exibir_subtitulo(texto):
      #os.system("cls") windows
      os.system('clear') # mac / linux
      print(texto)
      print()

def cadastrar_novo_restaurante():
      exibir_subtitulo("Cadastro de novos restaurantes")

      nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
      categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}:")
      dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}

      restaurantes.append(dados_do_restaurante)
      print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
      voltar_menu_principal()

def finalizar_app():
    exibir_subtitulo("Finalizando o app...\n")

def listar_restaurantes():
      exibir_subtitulo("Listar restaurantes")

      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'- {nome_restaurante} | {categoria} | {ativo}')

      voltar_menu_principal()

def alternar_estado_restaurante():
      exibir_subtitulo("Alternando estado do restaurante")

      nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
      restaurante_encontrado = False

      for restaurante in restaurantes:
       if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (f"""O restaurante {nome_restaurante} foi ativado com sucesso"""
            if restaurante['ativo'] 
            else f"""O restaurante {nome_restaurante} foi desativado com sucesso""")
            print(mensagem)

      if not restaurante_encontrado:
            print("O restaurante não foi encontrado")
            

      voltar_menu_principal()


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
                        alternar_estado_restaurante()

                  case 4:
                  #os.system("cls") windows
                        os.system("clear") # mac / linux
                        finalizar_app()

                  case _:
                        opcao_invalida()
            
      except:
             opcao_invalida()

def main():
    os.system('clear')
    nome_programa()
    mostra_opcoes()
    escolhe_opcao()

if __name__ == "__main__":
    main()