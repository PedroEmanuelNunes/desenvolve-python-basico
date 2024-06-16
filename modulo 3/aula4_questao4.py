# Entrada de dados
distancia = float(input("Insira a distância da entrega em quilômetros: "))
peso = float(input("Insira o peso do pacote em quilogramas: "))

# Processamento 
# Calculando o valor base do frete de acordo com a distância
if distancia <= 100:
    valor_frete = 1.00 * peso
else:
    if distancia <= 300:
        valor_frete = 1.50 * peso
    else:
        valor_frete = 2.00 * peso
# Adicionando a taxa adicional para pacotes com peso superior a 10 kg
if peso > 10:
    valor_frete += 10

#saída
print(f"O valor do frete é: R${valor_frete:.2f}")
