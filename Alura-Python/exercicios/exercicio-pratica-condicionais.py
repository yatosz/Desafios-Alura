#!/usr/bin/env python3
#Exercícios
# 1 - Solicite ao usuário que insira um número e, em seguida, 
#     use uma estrutura if else para determinar se o número é par ou ímpar.

numero_inserido = int(input("Insira um número: "))

if numero_inserido % 2 == 0:
    print(f"o número {numero_inserido} par")

else:
    print(f"o número {numero_inserido} impar")


# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar 
#      a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.
    
idade_usuario = int(input("Informe sua idade: "))

if idade_usuario <= 12:
    print("Criança")

elif idade_usuario >= 13 and idade_usuario <= 18:
    print("Adolescente")

else:
    print("Adulto")
    

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário
# e a senha fornecidos correspondem aos valores esperados determinados por você.

login_user = input("Informe o usuário: ")
senha_user = input("Informe a senha: ")

if login_user and senha_user == "igor123":
    print("Acesso autorizado")

else:
    print("Acesso negado")


# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else
# para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

cordenada_x = int(input("Informe a cordenada para x:"))
cordenada_y = int(input("Informe a cordenada para y: "))

if cordenada_x > 0 and cordenada_y > 0:
    print("Primeiro Quadrante")

elif cordenada_x < 0 and cordenada_y > 0:
    print("Segundo Quadrante")

elif cordenada_x < 0 and cordenada_y < 0:
    print("Terceiro Quadrante")

elif cordenada_x > 0 and cordenada_y < 0:
    print("Quarto Quadrante")

else:
    print("o ponto está localizado no eixo ou origem")