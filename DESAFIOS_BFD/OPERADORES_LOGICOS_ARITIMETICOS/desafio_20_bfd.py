#Pergunte a quantidade de produtos no estoque e se é produto essencial (True/False).
#Reponha se for essencial ou a quantidade for menor que 10.

#Entrada de dados pelo usuario com quantidade e se essencial o produto
quant_produto = int(input("Informe a quantidade do produto em estoque: "))
se_essecial = str(input("Se essencial digite [S] ou [N] caso não: ")).upper().strip()

#Verifica se deve repor
verifica_repor = quant_produto < 10 or se_essecial == "S"

#Imprime se repor ou não
print(f"O produto informado deve ser reposto em estoque? {verifica_repor}")
