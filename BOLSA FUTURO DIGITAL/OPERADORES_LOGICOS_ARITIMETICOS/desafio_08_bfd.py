#PEÇA UM VALOR DE HORA E CONVERTA UM VALOR DE HORAS PARA MINUTOS

#Entrada de dados pelo usuario informando a quantidade de horas que deseja verificar os minutos
quant_horas = float(input("Informe a quantidade de horas para obter os minutos: "))

#Verificando quantos minutos tem na quantidade de horas informada
quant_minutos = quant_horas * 60

print(f"{quant_horas} horas tem {quant_minutos} minutos.")
