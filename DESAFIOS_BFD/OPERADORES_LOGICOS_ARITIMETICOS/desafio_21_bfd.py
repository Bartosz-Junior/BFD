#Solicite a altura e o peso, e verifique se o IMC está fora da faixa saudável (18.5 a 24.9)

#Entrada de dados do usuario com peso e altura do usuario
peso = float(input("Informe seu peso em Kg: "))
altura = float(input("Informe sua altura em metros: "))

#Calculo do IMC para classificar a faixa de saude
calculo_imc = peso / (altura ** 2)

#verificando se o usuario esta na faixa de saude.
imc = calculo_imc >= 18.5 and calculo_imc <=24.9

#Imprimindo o valor do IMC do usuario, se estiver na faixa de saude será informado.
print(f"Você se classifica na faixa de saúde de acordo com o seu IMC? {imc}")
