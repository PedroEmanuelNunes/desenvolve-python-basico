# Entrada
avaliacao = int(input("Insira a avaliação do filme (de 1 a 5): "))

# Processamento
if avaliacao == 5:
    mensagem = "Excelente!"
else:
    if avaliacao == 4:
        mensagem = "Muito Bom!"
    else:
        if avaliacao == 3:
            mensagem = "Bom!"
        else:
            if avaliacao == 2:
                mensagem = "Regular."
            else:
                if avaliacao == 1:
                    mensagem = "Ruim."
                else:
                    mensagem = "Avaliação inválida. Por favor, insira um número de 1 a 5."

# saída
print(mensagem)

