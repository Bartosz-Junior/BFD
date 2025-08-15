#SOLICITE A IDADE E SE O CLIENTE É VIP(TRUE/FALSE)
#PERMITA A ENTRADA SE FOR MAIOR DE IDADE E VIP
#EXIBA UMA MENSAGEM PERSONALIZADA

#Solicitando a idade do usuario
idade = int(input("Informe sua idade: "))

#Se é VIP ou não
se_vip = str(input("Você é um usuário VIP? [S/N]: ")).upper().strip()

#Analisando se o usuario é ou não VIP e maior de idade
verifica_entrada = idade >= 18 and se_vip == "S"

#Imprimindo se é permitido entrar no evento
print(f"O usuário informado pode acessar o envento? {verifica_entrada}")
