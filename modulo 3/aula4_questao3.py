# Entrada de dados
ano = int(input("Insira um ano: "))

# Processamento
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    mensagem = "Bissexto"
else:
    mensagem = "Não Bissexto"

# saída
print(mensagem)