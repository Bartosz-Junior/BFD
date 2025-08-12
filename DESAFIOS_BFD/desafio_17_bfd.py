#Peça a idade e se tem carteira de motorista (True/False).
#Permita dirigir se idade ≥ 18 e tiver carteira.

#Entrada de dados do usuario com idade e se habilitado
idade = int(input("Informe sua idade: "))
se_habilitado = str(input("Você tem CNH? [S/N]: ")).upper().strip()

#Tratando dados para verificar se pode dirigir
verifica_dirigir = idade >= 18 and se_habilitado == "S"

#Imprime se o usuário pode dirigir.
print(f"Olá, você pode dirigir? {verifica_dirigir}")
