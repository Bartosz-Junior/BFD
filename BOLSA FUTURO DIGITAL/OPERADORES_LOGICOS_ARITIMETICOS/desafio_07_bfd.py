#PEÇA A BASE E A ALTURA DE UM TRIANGULO E CALCULE SUA AREA

#Entrada de dados do usuario base e altura para calculo da area do triangulo
base_triangulo = float(input("Informe o valor da base do triangulo que deseja calcular a área: "))
altura_triangulo = float(input("Informe o valor da altura do triangulo que deseja calcular a área: "))

#Calculando a área do triangulo
area_triangulo = (base_triangulo * altura_triangulo) / 2

#Imprimindo o valor da area do triangulo:
print(f"O triangulo de base {base_triangulo:.2f}cm e altura {altura_triangulo:.2f}cm tem área {area_triangulo:.2f}cm².")
