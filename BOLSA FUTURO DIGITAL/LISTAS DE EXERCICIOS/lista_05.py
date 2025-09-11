import math
import statistics

#1. Crie uma função saudacao() que receba um nome como parâmetro e exiba "Olá, <nome>!".

def saudacao(nome):
    print(f"Olá, {nome}!")

#2. Escreva uma função soma(a, b) que retorne a soma de dois números.
def soma(a, b,):
    print(a + b)

#3. Faça uma função par_ou_impar(n) que retorne "Par" se o número for par e "Ímpar" caso contrário.

def par_impar(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

#4. Crie uma função dobro_lista(lista) que receba uma lista de números e retorne outra lista 
# com cada número dobrado.

def dobro_lista(lista):
    nova_lista = []
    for numero in lista:
        nova_lista.append(numero * 2)
    print(nova_lista)

#5. Explique, em código, a diferença entre uma 
# variável global e uma variável local.

variavel_global = "A variavel global é acessada em qualquer parte do código"

def teste_var():
    variavel_local = "Váriavel local só acesso dentro desta função, por exemplo."
    print(variavel_global)
    print(variavel_local)

def teste_var_local():
    print(variavel_global)
    print("Aqui não pega a varivel local da outra função ""teste_var_local""")

#6. Crie uma função media(*notas) que receba várias notas
#  (usando parâmetros variáveis) e retorne a média.

def media(*notas):
    media = sum(notas)/len(notas)
    print(media)

#7. Escreva uma função calculadora(a, b, operacao) que receba dois
#  números e uma operação ("+", "-", "*", "/") e retorne o resultado.

def calculadora(a, b, operacao):
    if (operacao == "+"):
        print(f"A soma é {a + b}.")
    elif (operacao == "-"):
        print(f"A subtração é {a - b}.")
    elif (operacao == "/"):
        print(f"A divisão é {a / b}.")
    elif (operacao == "*"):
        print(f"A multiplicação é {a * b}.")

#8. Faça uma função eh_primo(n) que retorne True se o número for primo e 
# False caso contrário

def eh_primo(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
            else:
                return True

#9. Modularize o código da questão 7:
# Um arquivo calculadora.py com funções de operações.
# Um arquivo main.py que importa e usa essas funções.

import calculadora
import interface

'''while True:
    interface.menu()
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        calculadora.soma()
    elif escolha == 2:
        calculadora.subtracao()
    elif escolha == 3:
        calculadora.multiplicacao()
    elif escolha == 4:
        calculadora.divisao()
    elif escolha == 0:
        print("Saindo...")
        break'''

#10. Crie uma função palindromo(palavra) que retorne
# True se a palavra for um palíndromo, e False caso contrário.

def palindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    else:
        return False

#11. Implemente uma calculadora modularizada que:
#- Tenha um módulo com funções matemáticas (soma, subtracao, multiplicacao, divisao).
#- Tenha um módulo interface.py para interagir com o usuário.
# - O main.py deve importar os módulos e executar o programa.

'''while True:
    interface.menu()
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        calculadora.soma()
    elif escolha == 2:
        calculadora.subtracao()
    elif escolha == 3:
        calculadora.multiplicacao()
    elif escolha == 4:
        calculadora.divisao()
    elif escolha == 0:
        print("Saindo...")
        break'''

#12. Crie um sistema de login modularizado:
#- Um módulo usuarios.py que armazene um dicionário de usuários e senhas.
#- Um módulo autenticacao.py com funções registrar_usuario e login.
#- Um main.py que permita ao usuário registrar e autenticar usuários.

import autenticacao
'''
while True:
    try:
        autenticacao.menu()
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1 :
            autenticacao.login()
        elif escolha == 2:
            autenticacao.registrar_usuario()
        elif escolha == 0:
            print("Saindo...")
            break
    except ValueError:
        print("Opção inválida!")
'''

#13. Implemente uma função fibonacci(n) que retorne os n primeiros números da sequência de Fibonacci.
#  Depois, modularize em dois arquivos:
#- funcoes.py (com a lógica).
#- main.py (com input do usuário).
'''
import funcao_fibonacci

funcao_fibonacci.fibonacci()
'''

#14. Desenvolva uma função estatística(lista) que retorne um dicionário com: média, mediana, 
# maior e menor valor da lista.

def estatistica(lista):
    print(f"O maior valor é: {max(lista)}")
    print(f"O menor valor é: {min(lista)}")
    print(f"A mediana é {statistics.median(lista)}")
    print(f"A média é {statistics.mean(lista)}")


#15. Crie um programa modularizado chamado Mini-Sistema de Alunos:
#- Módulo alunos.py: funções para adicionar aluno, remover e listar.
#- Módulo notas.py: funções para lançar notas e calcular médias.
#- main.py: menu interativo para o usuário acessar as opções.

