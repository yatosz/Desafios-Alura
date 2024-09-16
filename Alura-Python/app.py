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
      linha = '-' * (len(texto) + 2)
      print(linha)
      print(texto)
      print(linha)
      print()

def cadastrar_novo_restaurante():
      ''' Essa função é responsável por cadastrar um novo restaurante
      
      Inputs:
      - Nome do restaurante
      - Categoria

      Output:
      -Adiciona um novo restaurante e lista de restaurantes
      '''
      exibir_subtitulo("Cadastro de novos restaurantes")

      nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
      categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}:")
      dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}

      restaurantes.append(dados_do_restaurante)
      print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
      voltar_menu_principal()

def finalizar_app():
    '''Exibe mensagem de finalização do aplicativo!'''
    exibir_subtitulo("Finalizando o app...\n")

def listar_restaurantes():
      '''exibe o subtitulo.'''
      exibir_subtitulo("Listar restaurantes")

      '''Lista os nomes dos restaurantes na tela'''
      print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            #ljust | adiciona espaçamentos
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

      voltar_menu_principal()

def alternar_estado_restaurante():
      '''alterna entre estado do restaurante, entre ativado ou desativado
      
      Outputs:
      Exibe mensagem de sucesso da operação'''
      
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
      '''Solicita a opção para o usuário
      
      Outputs:
      Executa a opção escolhida pelo usuário'''
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
    '''Função inicial que inicia o programa'''
    os.system('clear')
    nome_programa()
    mostra_opcoes()
    escolhe_opcao()

if __name__ == "__main__":
    '''Main que chama a função/rotina Main'''
    main()